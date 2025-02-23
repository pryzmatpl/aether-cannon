import matplotlib.pyplot as plt
import numpy as np

def draw_pcb_layout():
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("Marx Generator PCB Layout (Concept Sketch)")
    
    # Draw capacitor banks
    for i in range(4):
        ax.add_patch(plt.Rectangle((2, 6 - i * 1.5), 2, 1, edgecolor='blue', facecolor='none', lw=2))
        ax.text(3, 6.5 - i * 1.5, f"C{i+1}", fontsize=12, ha='center', va='center', color='blue')
    
    # Draw resistors
    for i in range(4):
        ax.add_patch(plt.Rectangle((6, 6 - i * 1.5), 2, 1, edgecolor='green', facecolor='none', lw=2))
        ax.text(7, 6.5 - i * 1.5, f"R{i+1}", fontsize=12, ha='center', va='center', color='green')
    
    # Draw spark gaps
    for i in range(4):
        ax.plot([4, 6], [6.5 - i * 1.5, 6.5 - i * 1.5], 'r--', lw=2)
        ax.text(5, 6.6 - i * 1.5, "SG", fontsize=12, ha='center', va='center', color='red')
    
    # Draw HV input and output
    ax.plot([1, 2], [7.5, 7.5], 'k-', lw=3)
    ax.text(0.8, 7.5, "HV In", fontsize=12, ha='right', color='black')
    ax.plot([8, 9], [7.5, 7.5], 'k-', lw=3)
    ax.text(9.2, 7.5, "HV Out", fontsize=12, ha='left', color='black')
    
    # Draw ground connection
    ax.plot([5, 5], [0, 1], 'k-', lw=3)
    ax.text(5, 0.5, "Ground", fontsize=12, ha='center', va='bottom', color='black')
    
    plt.show()

draw_pcb_layout()
