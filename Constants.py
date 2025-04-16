# Constants.py

# --- Pygame Setup ---
Ancho = 800
Alto = 600
Blanco = (255, 255, 255)
Negro = (0, 0, 0)
Rojo = (255, 0, 0)
Azul = (0, 0, 255)
Verde = (0, 255, 0) # For effort mass

# --- Simulation ---
GRAVEDAD = 9.81
ESCALA = 20       # Pixels per meter (adjust as needed)
DT = 0.05         # Time step (smaller might be more stable)

# --- Masses ---
masa_carga_valor = 10.0  # Mass M (kg) - Load
masa_esfuerzo_valor = 3.0 # Mass m (kg) - Effort

# --- Components Sizes ---
radio_polea = 20
size_carga = (40, 40)
size_esfuerzo = (30, 30)

# --- Initial Positions (Example - Adjust these carefully!) ---
# Top support structure (for drawing and anchoring)
pos_soporte_y = 50
pos_soporte_inicio_x = 100
pos_soporte_fin_x = Ancho - 100

# Fixed Pulley (Pulley 0 in analysis) - Attached to support
pos_polea_fija = (Ancho // 2 - 100, pos_soporte_y + radio_polea) # Example X position

# Movable Pulleys (Cluster attached to Load) - Initial Y position
initial_movable_y = Alto // 2
pos_poleas_moviles = [
    (Ancho // 2 + 50, initial_movable_y),      # Top movable (P1)
    (Ancho // 2 + 50, initial_movable_y + 60), # Middle movable (P2)
    (Ancho // 2 + 50, initial_movable_y + 120) # Bottom movable (P3)
]
# Make sure movable pulleys are stored in a mutable list

# Load (Attached below movable pulleys)
pos_carga = (pos_poleas_moviles[-1][0] - size_carga[0] // 2, pos_poleas_moviles[-1][1] + radio_polea + 10) # Centered below last pulley

# Effort Mass (Hangs from fixed pulley rope)
pos_esfuerzo = (pos_polea_fija[0] - 150, Alto // 3) # Initial position

# Rope Anchor Points on Top Support (Relative to pulley X positions maybe)
# Based on diagram: Anchor1 -> P3 -> P0 -> P2 -> P1 -> Anchor2, Effort from P0
anclaje_1_x = pos_polea_fija[0] + 100 # Example
anclaje_2_x = pos_poleas_moviles[0][0] + 50 # Example
pos_anclaje_1 = (anclaje_1_x, pos_soporte_y)
pos_anclaje_2 = (anclaje_2_x, pos_soporte_y)


# --- State Variables (Initial) ---
# Store velocities globally or pass them around if preferred
velocidad_carga = 0.0 # Vertical velocity of the load (m/s, positive up)
# We derive effort velocity from load velocity

# --- Boundaries ---
limite_superior_carga = pos_soporte_y + radio_polea * 2 # Cannot hit fixed pulley support
limite_inferior_carga = Alto - size_carga[1] - 10
limite_superior_esfuerzo = pos_soporte_y + radio_polea * 2
limite_inferior_esfuerzo = Alto - size_esfuerzo[1] - 10