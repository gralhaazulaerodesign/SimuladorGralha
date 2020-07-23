# Generate dictionary with plane and takeoff data
# Ideally you should give all data (like on
# this example). If you don't use some of it, just give
# dummy data (zeros or anything).

from ADR.Core.data_manipulation import replace_forced_parameters

original_plane_parameters = {
    "plane_type": 'monoplane',

    "wing1_x": 0,
    "wing1_y": 0,
    "wing1_z": 0,
    "wing1_clmax_airfoil": 2.38,
    "wing1_airfoil1_name": "ca2013",
    "wing1_airfoil2_name": "ca2013",
    "wing1_airfoil3_name": "ca2013",
    "wing1_span1": 0.6500,
    "wing1_span2": 0.5000,
    "wing1_chord1": 0.5,
    "wing1_chord2": 0.5,
    "wing1_chord3": 0.28,
    "wing1_twist1": 0,
    "wing1_twist2": 0,
    "wing1_twist3": 0,
    "wing1_incidence": 4,


[MONOPLANO! ISSO AQUI PROVAVELMENTE TEM QUE EXCLUIR 

    "wing2_x": 0,
    "wing2_y": 0,
    "wing2_z": 0.6,
    "wing2_clmax_airfoil": 2.2,
    "wing2_airfoil1_name": "s1223",
    "wing2_airfoil2_name": "s1223",
    "wing2_airfoil3_name": "s1223",
    "wing2_span1": 0.8605,
    "wing2_span2": 0.3895,
    "wing2_chord1": 0.4,
    "wing2_chord2": 0.35,
    "wing2_chord3": 0.25,
    "wing2_twist1": 0,
    "wing2_twist2": 0,
    "wing2_twist3": 0,
    "wing2_incidence": 0,

ATÉ AQUI]


    "hs_x": -0.540,
    "hs_y": 0,
    "hs_z": 0.250,
    "hs_clmax_airfoil": 1.26,
    "hs_airfoil1_name": "sd7037",
    "hs_airfoil2_name": "sd7037",
    "hs_airfoil3_name": "sd7037",
    "hs_span1": 0.000,
    "hs_span2": 0.600,
    "hs_chord1": 0.350,
    "hs_chord2": 0.350,
    "hs_chord3": 0.350,
    "hs_twist1": 0,
    "hs_twist2": 0,
    "hs_twist3": 0,
    "hs_incidence": 7,


    "vs_x": -0.7,
    "vs_y": 0,
    "vs_z": 0,
    "vs_clmax_airfoil": 2.2,
    "vs_airfoil1_name": "s1223",
    "vs_airfoil2_name": "s1223",
    "vs_airfoil3_name": "s1223",
    "vs_span1": 0.1,
    "vs_span2": 0.1,
    "vs_chord1": 0.2,
    "vs_chord2": 0.2,
    "vs_chord3": 0.1,
    "vs_twist1": 0,
    "vs_twist2": 0,
    "vs_twist3": 0,
    "vs_incidence": 0,

    "motor_x": 0.2,
    "motor_z": 0,
    "static_thrust": 45,
    "linear_decay_coefficient": 1.1,

    "cg_x": -0.125,
    "cg_z": -0.04,

    "tpr_x": -0.155,
    "tpr_z": -0.150,

    "Iyy_TPR": 0.2,
    "CD_tp": 0.8,
    "S_tp": 0.001,
    "CD_fus": 0.6,
    "S_fus": 0.02,
    "u_k": 0.05
}

original_performance_parameters = {
    "rho_air": 1.1, # Densidade do ar [kg/m^3]
    "dist_max": 50, # Distancia maxima de decolagem pelo regulamento [m]
    "offset_pilot": 5 # Distancia antes do fim da pista em que o piloto aciona o profundor [m]
}

def plane_parameters(forced_plane_parameters):
    mixed_plane_parameters = replace_forced_parameters(original_plane_parameters, forced_plane_parameters)
    return mixed_plane_parameters

def performance_parameters(forced_performance_parameters):
    mixed_performance_parameters = replace_forced_parameters(original_performance_parameters, forced_performance_parameters)
    return mixed_performance_parameters


