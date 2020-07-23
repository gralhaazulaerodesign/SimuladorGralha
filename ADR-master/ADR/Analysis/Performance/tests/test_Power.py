from ADR.Analysis.Performance.Power import Power
from ADR.Core.data_manipulation import dict_to_dataframe
from ADR.Components.Plane import Plane
import pytest
import numpy.testing as npt
import pandas as pd


@pytest.fixture
def power():
    plane_data = {
        "plane_type": "biplane",
        "wing1_x": 0,
        "wing1_y": 0,
        "wing1_z": 0,
        "wing1_clmax_airfoil": 2.5,
        "wing1_airfoil1_name": "s1223",
        "wing1_airfoil2_name": "s1223",
        "wing1_airfoil3_name": "s1223",
        "wing1_span1": 1,
        "wing1_span2": 1,
        "wing1_chord1": 0.35,
        "wing1_chord2": 0.33,
        "wing1_chord3": 0.30,
        "wing1_twist1": 10,
        "wing1_twist2": 5,
        "wing1_twist3": 3,
        "wing1_incidence": 1,
        "wing1_CM_ca": 0.08,
        "wing2_x": 0,
        "wing2_y": 0,
        "wing2_z": 0,
        "wing2_clmax_airfoil": 2.8,
        "wing2_airfoil1_name": "s1223",
        "wing2_airfoil2_name": "s1223",
        "wing2_airfoil3_name": "s1223",
        "wing2_span1": 1.10,
        "wing2_span2": 1.10,
        "wing2_chord1": 0.40,
        "wing2_chord2": 0.35,
        "wing2_chord3": 0.33,
        "wing2_twist1": 5,
        "wing2_twist2": 3,
        "wing2_twist3": 0,
        "wing2_incidence": 1,
        "wing2_CM_ca": 0.10,
        "hs_x": 0.9,
        "hs_y": 0,
        "hs_z": 0,
        "hs_clmax_airfoil": 2.1,
        "hs_airfoil1_name": "sd7037",
        "hs_airfoil2_name": "sd7037",
        "hs_airfoil3_name": "sd7037",
        "hs_span1": 0.30,
        "hs_span2": 0.30,
        "hs_chord1": 0.24,
        "hs_chord2": 0.24,
        "hs_chord3": 0.24,
        "hs_twist1": 0,
        "hs_twist2": 0,
        "hs_twist3": 0,
        "hs_incidence": 0,
        "hs_CM_ca": 0.06,
        "motor_x": 0,
        "motor_y": 0,
        "motor_z": 0,
        "static_thrust": 0,
        "linear_decay_coefficient": -0.15,
        "cg_x": 0.11,
        "cg_z": 0.01,
        "tpr_x": 0.13,
        "tpr_z": -0.08,
        "Iyy_TPR": 1,
        "CD_tp": 1,
        "S_tp": 1,
        "CD_fus": 1,
        "S_fus": 1,
        "u_k": 1,
    }

    plane = Plane(plane_data)

    performance_parameters = {
        "rho_air": 1.1,  # Densidade do ar [kg/m^3]
        "dist_max": 45,  # Distancia maxima de decolagem pelo regulamento [m]
        # Distancia antes do fim da pista em que o piloto aciona o profundor [m]
        "offset_pilot": 5,
    }

    power = Power(plane, performance_parameters)
    return power


def test_power_required(power):
    power_required_check = {
        3.693459: 55.925256,
        3.793459: 60.549268,
        3.893459: 65.434352,
        3.993459: 70.606824,
        4.093459: 76.044941,
        4.193459: 81.755353,
        4.293459: 87.744713,
        4.393459: 94.019673,
        4.493459: 100.586884,
        4.593459: 107.452999,
        4.693459: 114.624669,
        4.793459: 122.108547,
        4.893459: 129.911284,
        4.993459: 138.039533,
        5.093459: 146.499945,
        5.193459: 155.299173,
        5.293459: 164.443868,
        5.393459: 173.940683,
        5.493459: 183.796268,
        5.593459: 194.017277,
        5.693459: 204.610362,
        5.793459: 215.582173,
        5.893459: 226.939364,
        5.993459: 238.688586,
        6.093459: 250.836491,
        6.193459: 263.389731,
        6.293459: 276.354958,
        6.393459: 289.738825,
        6.493459: 303.547982,
        6.593459: 317.789082,
        6.693459: 332.468778,
        6.793459: 347.593720,
        6.893459: 363.170561,
        6.993459: 379.205954,
        7.093459: 395.706549,
        7.193459: 412.678999,
        7.293459: 430.129955,
        7.393459: 448.066071,
        7.493459: 466.493997,
        7.593459: 485.420386,
        7.693459: 504.851889,
        7.793459: 524.795160,
        7.893459: 545.256849,
        7.993459: 566.243608,
        8.093459: 587.762090,
        8.193459: 609.818947,
        8.293459: 632.420830,
        8.393459: 655.574392,
        8.493459: 679.286284,
        8.593459: 703.563159,
        8.693459: 728.411668,
    }

    df_power_required_check = dict_to_dataframe(
        power_required_check, "Power required", "Velocity"
    )

    alpha_velocity_check = {
        3.693459: -9.4,
        3.793459: -9.7,
        3.893459: -9.9,
        3.993459: -9.9,
        4.093459: -9.9,
        4.193459: -9.9,
        4.293459: -9.9,
        4.393459: -9.9,
        4.493459: -9.9,
        4.593459: -9.9,
        4.693459: -9.9,
        4.793459: -9.9,
        4.893459: -9.9,
        4.993459: -9.9,
        5.093459: -9.9,
        5.193459: -9.9,
        5.293459: -9.9,
        5.393459: -9.9,
        5.493459: -9.9,
        5.593459: -9.9,
        5.693459: -9.9,
        5.793459: -9.9,
        5.893459: -9.9,
        5.993459: -9.9,
        6.093459: -9.9,
        6.193459: -9.9,
        6.293459: -9.9,
        6.393459: -9.9,
        6.493459: -9.9,
        6.593459: -9.9,
        6.693459: -9.9,
        6.793459: -9.9,
        6.893459: -9.9,
        6.993459: -9.9,
        7.093459: -9.9,
        7.193459: -9.9,
        7.293459: -9.9,
        7.393459: -9.9,
        7.493459: -9.9,
        7.593459: -9.9,
        7.693459: -9.9,
        7.793459: -9.9,
        7.893459: -9.9,
        7.993459: -9.9,
        8.093459: -9.9,
        8.193459: -9.9,
        8.293459: -9.9,
        8.393459: -9.9,
        8.493459: -9.9,
        8.593459: -9.9,
        8.693459: -9.9,
    }

    df_alpha_velocity_check = dict_to_dataframe(
        alpha_velocity_check, "Alpha", "Velocity"
    )

    thrust_velocity_check = {
        3.693459: 15.141704,
        3.793459: 15.961495,
        3.893459: 16.806228,
        3.993459: 17.680620,
        4.093459: 18.577186,
        4.193459: 19.495925,
        4.293459: 20.436837,
        4.393459: 21.399922,
        4.493459: 22.385181,
        4.593459: 23.392613,
        4.693459: 24.422218,
        4.793459: 25.473996,
        4.893459: 26.547948,
        4.993459: 27.644073,
        5.093459: 28.762371,
        5.193459: 29.902842,
        5.293459: 31.065487,
        5.393459: 32.250305,
        5.493459: 33.457296,
        5.593459: 34.686460,
        5.693459: 35.937797,
        5.793459: 37.211308,
        5.893459: 38.506992,
        5.993459: 39.824849,
        6.093459: 41.164880,
        6.193459: 42.527084,
        6.293459: 43.911461,
        6.393459: 45.318011,
        6.493459: 46.746734,
        6.593459: 48.197631,
        6.693459: 49.670701,
        6.793459: 51.165944,
        6.893459: 52.683360,
        6.993459: 54.222950,
        7.093459: 55.784713,
        7.193459: 57.368649,
        7.293459: 58.974758,
        7.393459: 60.603041,
        7.493459: 62.253496,
        7.593459: 63.926125,
        7.693459: 65.620928,
        7.793459: 67.337903,
        7.893459: 69.077052,
        7.993459: 70.838374,
        8.093459: 72.621869,
        8.193459: 74.427538,
        8.293459: 76.255379,
        8.393459: 78.105394,
        8.493459: 79.977582,
        8.593459: 81.871944,
        8.693459: 83.788479,
    }

    df_thrust_velocity_check = dict_to_dataframe(
        thrust_velocity_check, "Thrust required", "Velocity"
    )

    pd.testing.assert_frame_equal(
        power.power_required_df, df_power_required_check, check_less_precise=3
    )
    pd.testing.assert_frame_equal(
        power.alpha_df, df_alpha_velocity_check, check_less_precise=3
    )
    pd.testing.assert_frame_equal(
        power.thrust_required_df, df_thrust_velocity_check, check_less_precise=3
    )


def test_power_available(power):
    thrust_available_check = {
        3.693459: 0.554019,
        3.793459: 0.569019,
        3.893459: 0.584019,
        3.993459: 0.599019,
        4.093459: 0.614019,
        4.193459: 0.629019,
        4.293459: 0.644019,
        4.393459: 0.659019,
        4.493459: 0.674019,
        4.593459: 0.689019,
        4.693459: 0.704019,
        4.793459: 0.719019,
        4.893459: 0.734019,
        4.993459: 0.749019,
        5.093459: 0.764019,
        5.193459: 0.779019,
        5.293459: 0.794019,
        5.393459: 0.809019,
        5.493459: 0.824019,
        5.593459: 0.839019,
        5.693459: 0.854019,
        5.793459: 0.869019,
        5.893459: 0.884019,
        5.993459: 0.899019,
        6.093459: 0.914019,
        6.193459: 0.929019,
        6.293459: 0.944019,
        6.393459: 0.959019,
        6.493459: 0.974019,
        6.593459: 0.989019,
        6.693459: 1.004019,
        6.793459: 1.019019,
        6.893459: 1.034019,
        6.993459: 1.049019,
        7.093459: 1.064019,
        7.193459: 1.079019,
        7.293459: 1.094019,
        7.393459: 1.109019,
        7.493459: 1.124019,
        7.593459: 1.139019,
        7.693459: 1.154019,
        7.793459: 1.169019,
        7.893459: 1.184019,
        7.993459: 1.199019,
        8.093459: 1.214019,
        8.193459: 1.229019,
        8.293459: 1.244019,
        8.393459: 1.259019,
        8.493459: 1.274019,
        8.593459: 1.289019,
        8.693459: 1.304019,
    }

    df_thrust_available_check = dict_to_dataframe(
        thrust_available_check, "Thrust available", "Velocity"
    )

    power_available_check = {
        3.693459: 2.046245,
        3.793459: 2.158549,
        3.893459: 2.273853,
        3.993459: 2.392157,
        4.093459: 2.513460,
        4.193459: 2.637764,
        4.293459: 2.765068,
        4.393459: 2.895372,
        4.493459: 3.028676,
        4.593459: 3.164979,
        4.693459: 3.304283,
        4.793459: 3.446587,
        4.893459: 3.591891,
        4.993459: 3.740194,
        5.093459: 3.891498,
        5.193459: 4.045802,
        5.293459: 4.203106,
        5.393459: 4.363409,
        5.493459: 4.526713,
        5.593459: 4.693017,
        5.693459: 4.862321,
        5.793459: 5.034624,
        5.893459: 5.209928,
        5.993459: 5.388232,
        6.093459: 5.569536,
        6.193459: 5.753839,
        6.293459: 5.941143,
        6.393459: 6.131447,
        6.493459: 6.324751,
        6.593459: 6.521054,
        6.693459: 6.720358,
        6.793459: 6.922662,
        6.893459: 7.127966,
        6.993459: 7.336269,
        7.093459: 7.547573,
        7.193459: 7.761877,
        7.293459: 7.979181,
        7.393459: 8.199484,
        7.493459: 8.422788,
        7.593459: 8.649092,
        7.693459: 8.878396,
        7.793459: 9.110700,
        7.893459: 9.346003,
        7.993459: 9.584307,
        8.093459: 9.825611,
        8.193459: 10.069915,
        8.293459: 10.317218,
        8.393459: 10.567522,
        8.493459: 10.820826,
        8.593459: 11.077130,
        8.693459: 11.336433,
    }

    df_power_available_check = dict_to_dataframe(
        power_available_check, "Power available", "Velocity"
    )

    pd.testing.assert_frame_equal(
        power.thrust_available_df, df_thrust_available_check, check_less_precise=3
    )
    pd.testing.assert_frame_equal(
        power.power_available_df, df_power_available_check, check_less_precise=3
    )


def test_power_excess(power):
    power_excess_check = {
        3.693458584650559: -53.87901072296934,
        3.7934585846505593: -58.39071923177715,
        3.8934585846505594: -63.16049866668177,
        3.9934585846505595: -68.21466776637739,
        4.093458584650559: -73.53148059043242,
        4.19345858465056: -79.11758911028298,
        4.29345858465056: -84.97964529736497,
        4.39345858465056: -91.12430112311439,
        4.4934585846505595: -97.55820855896721,
        4.59345858465056: -104.28801957635953,
        4.6934585846505605: -111.32038614672733,
        4.79345858465056: -118.66196024150648,
        4.89345858465056: -126.31939383213309,
        4.99345858465056: -134.2993388900432,
        5.093458584650561: -142.60844738667276,
        5.1934585846505605: -151.2533712934577,
        5.29345858465056: -160.24076258183413,
        5.393458584650561: -169.57727322323802,
        5.493458584650561: -179.26955518910538,
        5.593458584650561: -189.3242604508721,
        5.6934585846505605: -199.74804097997426,
        5.793458584650561: -210.54754874784794,
        5.893458584650562: -221.72943572592908,
        5.993458584650561: -233.30035388565358,
        6.093458584650561: -245.26695519845754,
        6.193458584650561: -257.6358916357771,
        6.293458584650562: -270.4138151690479,
        6.393458584650562: -283.60737776970626,
        6.493458584650561: -297.22323140918803,
        6.593458584650562: -311.26802805892925,
        6.693458584650562: -325.74841969036595,
        6.793458584650562: -340.671058274934,
        6.893458584650562: -356.04259578406953,
        6.993458584650562: -371.8696841892086,
        7.093458584650563: -388.15897546178707,
        7.193458584650562: -404.917121573241,
        7.293458584650562: -422.1507744950062,
        7.3934585846505625: -439.86658619851903,
        7.493458584650563: -458.0712086552154,
        7.593458584650563: -476.77129383653096,
        7.693458584650562: -495.9734937139021,
        7.793458584650562: -515.6844602587644,
        7.893458584650563: -535.9108454425548,
        7.993458584650563: -556.6593012367081,
        8.093458584650563: -577.936479612661,
        8.193458584650562: -599.7490325418494,
        8.293458584650564: -622.1036119957093,
        8.393458584650563: -645.0068699456767,
        8.493458584650563: -668.465458363187,
        8.593458584650563: -692.4860292196771,
        8.693458584650564: -717.0752344865831,
    }

    df_power_excess_check = dict_to_dataframe(
        power_excess_check, "Power excess", "Velocity"
    )

    pd.testing.assert_frame_equal(
        power.power_excess_df, df_power_excess_check, check_less_precise=3
    )


def test_get_V_min_max(power):

    v_min_check = 3.693458584650559
    v_max_check = 8.693458584650564

    npt.assert_almost_equal(power.plane.V_min, v_min_check, decimal=3)
    npt.assert_almost_equal(power.plane.V_max, v_max_check, decimal=3)