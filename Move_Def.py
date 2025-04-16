import Constants
import math # For potential future tangent calculations

# Use a global or pass/return velocity if needed
# global velocidad_carga  -> Defined in Constants or main script

def actualizar_movimiento():
    # Use the global velocity defined elsewhere
    global velocidad_carga # m/s, positive UP for the load

    m = Constants.masa_esfuerzo_valor # Effort mass
    M = Constants.masa_carga_valor    # Load mass

    # Calculate acceleration of the LOAD (R) upwards
    denominator = M + 16 * m
    if denominator == 0:
        a_R = 0 # Prevent division by zero
    else:
        # Ensure GRAVEDAD is positive
        g = abs(Constants.GRAVEDAD)
        # Positive a_R means load accelerates UP
        a_R = g * (4 * m - M) / denominator

    # Update load velocity (physics space)
    # v = v0 + a*t
    velocidad_carga += a_R * Constants.DT

    # Calculate displacement of LOAD for this time step (physics space)
    # dy = v*t (using updated velocity for Euler integration)
    dy_R_metros = velocidad_carga * Constants.DT

    # Convert displacement to pixels (Pygame space: positive Y is DOWN)
    # So positive dy_R_metros (up) means negative dy_pixels
    dy_R_pixels = -dy_R_metros * Constants.ESCALA

    # Calculate displacement of EFFORT (moves 4 times further, downwards if load moves up)
    dy_F_pixels = 4 * (-dy_R_pixels) # If load moves -10px (up), effort moves +40px (down)

    # --- Apply Movement and Boundaries ---

    # Tentative new positions
    nueva_carga_y = Constants.pos_carga[1] + dy_R_pixels
    nueva_esfuerzo_y = Constants.pos_esfuerzo[1] + dy_F_pixels

    # Store current movable pulley Y positions
    current_movable_ys = [p[1] for p in Constants.pos_poleas_moviles]
    nuevas_poleas_moviles_y = [y + dy_R_pixels for y in current_movable_ys]

    # Boundary Checks (Simplified - check load and effort)
    can_move = True
    # Check load boundaries
    if not (Constants.limite_superior_carga < nueva_carga_y < Constants.limite_inferior_carga):
        can_move = False
        velocidad_carga = 0 # Stop at boundary

    # Check effort boundaries
    if not (Constants.limite_superior_esfuerzo < nueva_esfuerzo_y < Constants.limite_inferior_esfuerzo):
         # If effort hits boundary, load should also stop (rope connects them)
        can_move = False
        velocidad_carga = 0 # Stop at boundary

    # Check if movable pulleys hit fixed pulley (basic check)
    if any(ny <= Constants.pos_polea_fija[1] + Constants.radio_polea for ny in nuevas_poleas_moviles_y):
         can_move = False
         velocidad_carga = 0 # Stop at boundary


    # --- Update Positions if Movement is Allowed ---
    if can_move:
        # Update Load position
        Constants.pos_carga = (Constants.pos_carga[0], nueva_carga_y)

        # Update Effort position
        Constants.pos_esfuerzo = (Constants.pos_esfuerzo[0], nueva_esfuerzo_y)

        # Update Movable Pulleys position (THEY MOVE WITH THE LOAD)
        for i in range(len(Constants.pos_poleas_moviles)):
            Constants.pos_poleas_moviles[i] = (Constants.pos_poleas_moviles[i][0], nuevas_poleas_moviles_y[i])

    # Note: Rope drawing happens separately in the drawing loop, based on
    # the *updated* positions of pulleys, anchors, load, and effort.
