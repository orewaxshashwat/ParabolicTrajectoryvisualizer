import numpy as np
import matplotlib.pyplot as plt

g = 9.8  # Acceleration due to gravity (m/s^2)

def simulate_projectile(u, theta_deg):
    """Calculates kinematic parameters and trajectory coordinates."""
    theta = np.radians(theta_deg)
    
    T = (2 * u * np.sin(theta)) / g
    H = (u**2 * (np.sin(theta)**2)) / (2 * g)
    R = (u**2 * np.sin(2 * theta)) / g
    
    t = np.linspace(0, T, num=300)
    x = u * np.cos(theta) * t
    y = (u * np.sin(theta) * t) - (0.5 * g * t**2)
    
    return x, y, T, H, R

# Enable interactive mode for real-time plotting
plt.ion()
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

ax1.set_title('Graph 1: Effect of Velocity (Fixed Angle)')
ax1.set_xlabel('Horizontal Distance, x (m)')
ax1.set_ylabel('Vertical Height, y (m)')
ax1.grid(True, linestyle='--', alpha=0.6)

ax2.set_title('Graph 2: Effect of Angle (Fixed Velocity)')
ax2.set_xlabel('Horizontal Distance, x (m)')
ax2.set_ylabel('Vertical Height, y (m)')
ax2.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.pause(0.1)

# ==========================================
# GRAPH 1: Fixed Angle, Real-time Velocity
# ==========================================
print("=== GRAPH 1: Fixed Angle, Variable Velocity ===")
theta_fixed = float(input("Enter fixed angle θ (degrees): "))
ax1.set_title(f'Effect of Velocity (Fixed θ = {theta_fixed}°)')
plt.pause(0.1)

print(f"\n{'u (m/s)':<10} {'Angle (deg)':<13} {'Time T (s)':<13} {'Max Height H (m)':<18} {'Range R (m)':<15}")
print("-" * 70)

while True:
    val = input("Enter velocity u (m/s) [or type 'next' for Graph 2]: ").strip().lower()
    if val == 'next':
        break
    try:
        u = float(val)
        x, y, T, H, R = simulate_projectile(u, theta_fixed)
        print(f"{u:<10.1f} {theta_fixed:<13.1f} {T:<13.2f} {H:<18.2f} {R:<15.2f}")
        
        ax1.plot(x, y, label=f'u = {u} m/s')
        
        # Recalculate limits and autoscale both axes properly
        ax1.relim()
        ax1.autoscale(enable=True, axis='both')
        ax1.set_xlim(left=0)
        ax1.set_ylim(bottom=0)
        ax1.legend()
        
        fig.canvas.draw()
        plt.pause(0.1)
    except ValueError:
        print("Invalid input. Enter a number or 'next'.")

# ==========================================
# GRAPH 2: Fixed Velocity, Real-time Angle
# ==========================================
print("\n=== GRAPH 2: Fixed Velocity, Variable Angle ===")
u_fixed = float(input("Enter fixed initial velocity u (m/s): "))
ax2.set_title(f'Effect of Angle (Fixed u = {u_fixed} m/s)')
plt.pause(0.1)

print(f"\n{'u (m/s)':<10} {'Angle (deg)':<13} {'Time T (s)':<13} {'Max Height H (m)':<18} {'Range R (m)':<15}")
print("-" * 70)

while True:
    val = input("Enter angle θ (degrees) [or type 'done' to finish]: ").strip().lower()
    if val == 'done':
        break
    try:
        angle = float(val)
        x, y, T, H, R = simulate_projectile(u_fixed, angle)
        print(f"{u_fixed:<10.1f} {angle:<13.1f} {T:<13.2f} {H:<18.2f} {R:<15.2f}")
        
        ax2.plot(x, y, label=f'θ = {angle}°')
        
        # Recalculate limits and autoscale both axes properly
        ax2.relim()
        ax2.autoscale(enable=True, axis='both')
        ax2.set_xlim(left=0)
        ax2.set_ylim(bottom=0)
        ax2.legend()
        
        fig.canvas.draw()
        plt.pause(0.1)
    except ValueError:
        print("Invalid input. Enter a number or 'done'.")

print("\nSimulation complete. Close the plot window to exit.")
plt.ioff()
plt.show()