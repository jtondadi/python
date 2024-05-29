from machine import Pin, ADC, Timer
import utime

# Initialize the potentiometer (connected to GP26)
pot = ADC(26)

# Initialize the button (connected to GP15)
button = Pin(15, Pin.IN, Pin.PULL_DOWN)

# Initialize the LED (optional, connected to GP16)
led = Pin(16, Pin.OUT)

# Initialize counter and state variables
counter = 0
running = False

# Function to read the potentiometer value and set the counter increment
def read_potentiometer():
    pot_value = pot.read_u16()
    increment = pot_value // 1000  # Scale the potentiometer value (0-65535) to a reasonable range
    return increment if increment > 0 else 1  # Ensure a minimum increment of 1

# Timer callback function to update the counter
def update_counter(timer):
    global counter, running
    if running:
        increment = read_potentiometer()
        counter += increment
        print("Counter:", counter)

# Button press handler
def button_handler(pin):
    global running
    running = not running  # Toggle the running state
    led.value(running)  # Turn the LED on/off based on the running state
    print("Running:", running)

# Set up a timer to call the update_counter function periodically (e.g., every 1 second)
timer = Timer()
timer.init(period=1000, mode=Timer.PERIODIC, callback=update_counter)

# Attach the button handler to the button press event
button.irq(trigger=Pin.IRQ_RISING, handler=button_handler)

print("Press the button to start/stop the counter.")
