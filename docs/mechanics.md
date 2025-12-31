# Enigma Rotor Mechanics

This document describes the mechanics of rotor movement in this implementation, including the classic "double step" behavior.

## Mechanics Overview

The implementation uses an **Observer Pattern** where rotors notify the `Enigma` machine when they step *away* from a turnover position.

1.  **Pre-Stepping (Double Step)**: Before processing each character, the machine checks for any "double steps" triggered in the previous turn. If a rotor (except the last one) was moved onto its turnover position by the previous rotor, it performs an extra rotation.
2.  **Regular Stepping**: The rightmost rotor (index 0) always increments its position for every character.
3.  **Turnover Propagation**: When a rotor increments and leaves its turnover position, it notifies the `Enigma` instance.
4.  **Observer Update**: The `Enigma` machine, acting as an observer, responds by incrementing the next rotor in the chain. If that next rotor lands on its own turnover position, it triggers a double step for the *next* character.

## Pseudocode

```python
# Logic executed for every character input in the Enigma machine
Function input_char(processed_char):
    # 1. Handle double-stepping from previous turn
    # This addresses the mechanical "kick" of the middle rotor
    For each rotor in rotors (except the last one):
        If rotor.double_step_triggered is True:
            rotor.increment_position()
            rotor.double_step_triggered = False

    # 2. Regular step of the first (rightmost) rotor
    rotors[0].increment_position()
    
    # 3. Process the character (scrambling path)
    Return process_scrambling(processed_char)

# Logic inside the Rotor class
Function Rotor.increment_position():
    # Advance the rotor by one position
    self.position = (self.position + 1) MOD alphabet_length
    
    # Check if the internal wiring has rotated past a turnover index
    # We notify the machine when the rotor MOVES to the position after a turnover
    For each turnover_index in self.turnover_indexes:
        If self.position == (turnover_index + 1) MOD alphabet_length:
            Notify_Enigma_Machine(self)

# Logic inside the Enigma machine (Observer response to notification)
Function Enigma.on_rotor_turnover(notifying_rotor):
    idx = index_of(notifying_rotor)
    
    # If there is a next rotor to the left, increment it
    If idx < last_rotor_index:
        next_rotor = rotors[idx + 1]
        next_rotor.increment_position()
        
        # If the next rotor is now AT its turnover position,
        # mark it to perform an extra "double step" on the next char input
        If next_rotor.position IN next_rotor.turnover_indexes:
            next_rotor.double_step_triggered = True
```
