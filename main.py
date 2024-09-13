# States of water program

# -------------------------
# Subprograms
# -------------------------
def water_state(centigrade):
    
  if centigrade <= 0:
    return 'solid'
  elif centigrade > 0 and centigrade < 100: 
    return 'liquid'
    
  elif centigrade > 100:
    return 'gas'

# -------------------------
# Main program
# -------------------------
temperature = int(input())
state = water_state(temperature)
print("The water is in a", state, "state.")
