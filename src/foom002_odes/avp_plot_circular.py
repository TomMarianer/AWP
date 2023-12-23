'''
AWP | Astrodynamics with Python by Alfonso Gonzalez
https://github.com/alfonsogonzalez/AWP
https://www.youtube.com/c/AlfonsoGonzalezSpaceEngineering

Fundamentals of Orbital Mechanics 2
Ordinary Differential Equations (ODEs) Solvers

Acceleration, Velocity and Position subplots script
for circular orbit
Try changing out the orbital parameters!
'''

from python_tools.Spacecraft import Spacecraft as SC
import python_tools.orbit_calculations as oc
import python_tools.plotting_tools as pt

import numpy as np
import matplotlib.pyplot as plt

plt.style.use('dark_background')
# plt.style.use('classic')

# Molniya orbital elements
# a = 6778.0
a = 20000.0
coes = [a, 0.0, 0.0, 0.0, 0.0, 0.0]

sc_config = {
    'coes': coes,
    'tspan': '2.5',
    'dt': 100.0
}

if __name__ == '__main__':
    sc = SC(sc_config)
    accels = np.zeros((sc.states.shape[0], 3))

    for n in range(sc.states.shape[0]):
        accels[n] = oc.two_body_ode(sc.ets[n], sc.states[n])[3:]

    positions = sc.states[:, :3]
    velocities = sc.states[:, 3:6]

    # point_idx = 0
    # # origin = np.tile(positions[0, :], reps=(3, 1))
    # origin = positions[point_idx, :]
    # accel_vector = accels[point_idx, :] #* 1e6 #* np.linalg.norm(origin)

    # fig = plt.figure()
    # # ax = fig.add_subplot(111)
    # # ax.plot(positions[:, 0], positions[:, 1])
    # # ax.quiver(origin[0], origin[1], accel_vector[0], accel_vector[1], scale=2e-2)
    # # # ax.quiver(origin[0], origin[1], accel_vector[0], accel_vector[1], arrow_length_ration=0.1)
    #
    # ax = fig.add_subplot(111, projection='3d')
    # ax.plot(positions[:, 0], positions[:, 1], positions[:, 2])
    # # ax.quiver(X=origin[0], Y=origin[1], Z=origin[2], U=accels[point_idx, 0], V=accels[point_idx, 1], W=accels[point_idx, 2])
    # ax.quiver(X=origin[0], Y=origin[1], Z=origin[2], U=accel_vector[0], V=accel_vector[1], W=accel_vector[2], length=1e4, arrow_length_ratio=0.3, normalize=True)
    # # ax.quiver(X=origin[0], Y=origin[1], Z=origin[2], U=accel_vector[0], V=accel_vector[1], W=accel_vector[2], length=1e6, arrow_length_ratio=1e-6)
    # ax.set_zlim(-20e4, 20e4)

    ax = pt.plot_orbits(
        [], args={'axes_no_fill': False, 'legend': False, 'show': False, 'return_axes': True, 'axes_custom': 20e3})
    # ax.quiver(X=origin[0], Y=origin[1], Z=origin[2], U=accel_vector[0], V=accel_vector[1], W=accel_vector[2],
    #           length=3e3, normalize=True)  # , arrow_length_ratio=0.3, normalize=True)
    # for point_idx in range(10):
    point_idx = 75
    ax.plot(
        positions[:point_idx + 1, 0], positions[:point_idx + 1, 1], positions[:point_idx + 1, 2],
        linewidth=3, color='m')
    origin = positions[point_idx, :]
    accel_vector = accels[point_idx, :]  # * 1e6 #* np.linalg.norm(origin)
    ax.quiver(X=origin[0], Y=origin[1], Z=origin[2], U=accel_vector[0], V=accel_vector[1], W=accel_vector[2],
              length=3e3, normalize=True)  # , arrow_length_ratio=0.3, normalize=True)
    plt.show()

    # rnorms = np.linalg.norm(sc.states[:, :3], axis=1)
    # vnorms = np.linalg.norm(sc.states[:, 3:6], axis=1)
    # anorms = np.linalg.norm(accels, axis=1)
    #
    # fig, (ax0, ax1, ax2) = plt.subplots(3, 1,
    #                                     figsize=(20, 10))
    #
    # ets = (sc.ets - sc.ets[0]) / 3600.0
    #
    # ax0.plot(ets, accels[:, 0], 'r', label=r'$a_x$')
    # ax0.plot(ets, accels[:, 1], 'g', label=r'$a_y$')
    # ax0.plot(ets, accels[:, 2], 'b', label=r'$a_z$')
    # ax0.plot(ets, anorms, 'm', label=r'$Norms$')
    # ax0.grid(linestyle='dotted')
    # ax0.set_xlim(left=0, right=ets[-1])
    # ax0.set_ylabel(r'Acceleration $(\dfrac{km}{s^2})$', fontsize=20)
    # ax0.legend(loc='upper center')
    #
    # ax1.plot(ets, sc.states[:, 3], 'r', label=r'$v_x$')
    # ax1.plot(ets, sc.states[:, 4], 'g', label=r'$v_y$')
    # ax1.plot(ets, sc.states[:, 5], 'b', label=r'$v_z$')
    # ax1.plot(ets, vnorms, 'm', label=r'$Norms$')
    # ax1.grid(linestyle='dotted')
    # ax1.set_xlim(left=0, right=ets[-1])
    # ax1.set_ylabel(r'Velocity $(\dfrac{km}{s})$', fontsize=20)
    # ax1.legend(loc='upper center')
    #
    # ax2.plot(ets, sc.states[:, 0], 'r', label=r'$r_x$')
    # ax2.plot(ets, sc.states[:, 1], 'g', label=r'$r_y$')
    # ax2.plot(ets, sc.states[:, 2], 'b', label=r'$r_z$')
    # ax2.plot(ets, rnorms, 'm', label=r'$Norms$')
    # ax2.grid(linestyle='dotted')
    # ax2.set_xlim(left=0, right=ets[-1])
    # ax2.set_ylabel(r'Position $(km)$', fontsize=20)
    # ax2.set_xlabel('Time (hours)')
    # ax2.legend(loc='upper right')
    #
    # # plt.tight_layout()
    # plt.show()

    # ax = sc.plot_3d(args={'axes_no_fill': False, 'legend': False, 'show': False, 'return_axes': True})
    plt.show()
    # pt.plot_orbits([sc.states[:, :3]], args={'axes_no_fill': False, 'legend': False, 'show': True}, vectors=accels)


    # fn = '/mnt/c/Users/alfon/AWP/foom2_ode_solvers/avp_circular_eq.png'
    # plt.savefig(fn, dpi=300)
