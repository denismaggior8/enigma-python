# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2025-12-16

### Added
- **Enigma K Support**: Added support for the Commercial Enigma K, including specific rotors (I, II, III) and Entry Wheel logic.
- **Enigma M4/M3 Support**: Enhanced support for `SettableReflector` (Thin reflectors) allowing ring settings and initial positions to be correctly configured and used.
- **XRay Visualization**: Added `XRay` class and `render_enigma_xray` function to visualize the internal state of the Enigma machine (rotors, wiring, current path).
- **Unit Tests**: Added comprehensive tests for `SettableReflector` and `XRay` class.

### Changed
- **BREAKING**: Renamed `set_scrambler_ring` to `set_ring` in `Settable` class (and subclasses like `Rotor`).
- **BREAKING**: `Settable` class refactored. `set_ring` is now abstract in some contexts or requires specific implementation in subclasses.
- **BREAKING**: Removed `EnigmaDEtw_QWERTZ` and `EnigmaKEtw_QWERTZ` classes. Use `EtwQWERTZ` logic or equivalent base classes instead.
- **Refactoring**: `Enigma` class logic updated to correctly handle ETW inverted wiring calculations.

### Removed
- **BREAKING**: `EnigmaDEtw_QWERTZ` and `EnigmaKEtw_QWERTZ` files and classes have been deleted.

### Fixed
- **M4 Example**: Fixed and re-recorded `examples/enigma_m4_demo.cast` to correctly demonstrate M4 functionality with accurate visual output.
- **Documentation**: Updated `README.md` to include the new asciinema demo.
