#!/bin/bash

# Simulate moving the mouse to the top of the screen to reveal the menu bar
/opt/homebrew/bin/cliclick m:0,0
sleep 0.3  # Adjust the delay as needed to ensure the menu bar is revealed

# Click the LetsVPN menu bar icon (adjust these coordinates)
/opt/homebrew/bin/cliclick c:913,12
sleep 0.3  # Adjust the delay to allow the menu to open

# Click the "Let's Go" or "Let's Stop" button (adjust these coordinates)
/opt/homebrew/bin/cliclick c:821,427

# Click the "Let's Go" or "Let's Stop" button (adjust these coordinates)
/opt/homebrew/bin/cliclick c:1439,404
