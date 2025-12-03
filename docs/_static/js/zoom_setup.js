// Wait for Mermaid to finish rendering before initializing zoom
function initializeSvgPanZoom() {
    // Find all Mermaid SVG elements
    var svgs = document.querySelectorAll(".mermaid svg");

    svgs.forEach(function (svg) {
        // Skip if already initialized
        if (svg.hasAttribute('data-zoom-initialized')) {
            return;
        }

        // Check if SVG has valid dimensions using multiple methods
        var bbox = null;
        try {
            bbox = svg.getBBox();
        } catch (e) {
            console.log('getBBox failed for SVG:', svg.id, e);
        }

        // Also check computed dimensions
        var rect = svg.getBoundingClientRect();
        var hasValidBBox = bbox && bbox.width > 0 && bbox.height > 0;
        var hasValidRect = rect && rect.width > 0 && rect.height > 0;

        if (!hasValidBBox && !hasValidRect) {
            console.log('SVG not ready yet (no valid dimensions):', svg.id);
            setTimeout(function () { initializeSvgPanZoomForElement(svg); }, 200);
            return;
        }

        initializeSvgPanZoomForElement(svg);
    });
}

function initializeSvgPanZoomForElement(svg) {
    if (!svg || svg.hasAttribute('data-zoom-initialized')) {
        return;
    }

    // Mark as initialized
    svg.setAttribute('data-zoom-initialized', 'true');

    // Ensure the SVG has an ID
    if (!svg.id) {
        svg.id = "mermaid-" + Math.random().toString(36).substr(2, 9);
    }

    // Initialize svg-pan-zoom
    try {
        svgPanZoom('#' + svg.id, {
            zoomEnabled: true,
            controlIconsEnabled: true,
            fit: true,
            center: true,
            minZoom: 0.1,
            maxZoom: 50,
            zoomScaleSensitivity: 0.3
        });

        // Adjust style to make it look better
        svg.style.maxWidth = "100%";
        svg.style.height = "600px";
        svg.parentElement.style.overflow = "visible";

        console.log('Initialized zoom for SVG:', svg.id);
    } catch (e) {
        console.error('Failed to initialize svg-pan-zoom:', e);
    }
}

// Start trying to initialize after DOM is loaded
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () {
        setTimeout(initializeSvgPanZoom, 500);
    });
} else {
    // DOM already loaded
    setTimeout(initializeSvgPanZoom, 500);
}

// Also observe for dynamically added SVGs
var observer = new MutationObserver(function (mutations) {
    mutations.forEach(function (mutation) {
        if (mutation.addedNodes.length) {
            mutation.addedNodes.forEach(function (node) {
                if (node.nodeName === 'svg' && node.closest('.mermaid')) {
                    setTimeout(function () { initializeSvgPanZoomForElement(node); }, 100); // Give it a moment to render
                } else if (node.querySelectorAll) {
                    node.querySelectorAll('.mermaid svg').forEach(function (svgNode) {
                        setTimeout(function () { initializeSvgPanZoomForElement(svgNode); }, 100);
                    });
                }
            });
        }
    });
});

// Start observing
if (document.body) {
    observer.observe(document.body, {
        childList: true,
        subtree: true
    });
} else {
    window.addEventListener('load', function () {
        observer.observe(document.body, {
            childList: true,
            subtree: true
        });
    });
}
