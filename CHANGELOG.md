# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [3.0.1] - 2026-01-06

### Changed
- **Refactoring**: Modified `Settable` class to use managed properties for `ring` and `position`. Setting these attributes now automatically triggers the corresponding `set_ring` and `set_position` logic.
### Fixed
- **Settable**: Fixed `reset_position` to correctly call `set_position(0)` instead of direct attribute assignment. This ensures that subclasses like `Rotor` correctly reset their `rotations_counter`.
- **DynamicTurnoverRotor**: Added explicit `reset_ring` override to ensure `turnover_indexes` are updated correctly when using `reset_ring()`.

## [3.0.0] - 2025-12-29

### Added
- **New Feature**: Introduced `DynamicTurnoverRotor` class to correctly model rotor turnover behavior in Commercial Enigma D.
  - Supports dynamic turnover formulas via injectable lambda functions.
- **Documentation**: Added `DynamicTurnoverRotor` to ReadTheDocs configuration and Class Diagrams.
  - Updated Class Diagram to reflect the `ring` property and global renaming of turnover terms.
- **Enigma D**: Enigma D rotors (I, II, III) now inherit from `DynamicTurnoverRotor` and explicitly pass their turnover calculation formula.
- **Logic**: Updated `DynamicTurnoverRotor` turnover calculation logic to be fully dynamic via injectable functions.
- **Documentation**: Renamed "Notch" column to "Turnover" in all machine specification tables in generic documentation.
- **Class Diagram**: Updated all class definitions to use `turnover_indexes`.

## [2.0.2] - 2025-12-21

### Changed
- **Refactoring**: Updated `Swappable` class to be MicroPython compliant.

## [2.0.1] - 2025-12-17

### Fixed
- **Cleanup**: Removed `EnigmaDEtw_QWERTZ.py` and `EnigmaKEtw_QWERTZ.py` which were intended to be removed in 2.0.0.
- **Tests**: Removed redundant tests related to the deleted classes.

## [2.0.0] - 2025-12-16

### Added
- **Enigma K Support**: Added support for the Commercial Enigma K, including specific rotors (I, II, III) and Entry Wheel logic.
- **Unit Tests**: Added comprehensive tests for `SettableReflector` and `XRay` class.

### Changed
- **Enigma M4/M3**: Enhanced `SettableReflector` support to allow correct ring settings and initial positions for Thin reflectors.
- **XRay**: Updated visualization to support the new `SettableReflector` class.
- **BREAKING**: Renamed `set_scrambler_ring` to `set_ring` in `Settable` class (and subclasses like `Rotor`).
- **BREAKING**: `Settable` class refactored. `set_ring` is now abstract in some contexts or requires specific implementation in subclasses.
- **BREAKING**: Removed `EnigmaDEtw_QWERTZ` and `EnigmaKEtw_QWERTZ` classes. Use `EtwQWERTZ` logic or equivalent base classes instead.
- **Refactoring**: `Enigma` class logic updated to correctly handle ETW inverted wiring calculations.

### Removed
- **BREAKING**: `EnigmaDEtw_QWERTZ` and `EnigmaKEtw_QWERTZ` files and classes have been deleted.

### Fixed
- **M4 Example**: Fixed and re-recorded `examples/enigma_m4_demo.cast` to correctly demonstrate M4 functionality with accurate visual output.
- **Documentation**: Updated `README.md` to include the new asciinema demo.
