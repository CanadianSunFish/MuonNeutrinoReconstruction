#####################
#
# Contains CNN Model
#
####################


### Build The Network ##

import math

from keras import Model
from keras import Input
from keras import layers
from keras import backend as K
from tensorflow.python.ops import clip_ops
from tensorflow.python.framework import constant_op


def floatx():
    _FLOATX = "float32"
    return _FLOATX


def scaled_sigmoid(x):
    scale = math.pi
    print("using scaled_sigmoid activation function", scale)

    return K.sigmoid(x) * scale


def custom_activation(x, max_value=1, threshold=-1):
    """Rectified linear unit.
    With default values, it returns element-wise `max(x, 0)`.
    Otherwise, it follows:
    `f(x) = max_value` for `x >= max_value`,
    `f(x) = x` for `threshold <= x < max_value`,
    `f(x) = threshold` otherwise.
    Arguments:
        x: A tensor or variable.
        max_value: float. Saturation threshold.
        threshold: float. Threshold value for thresholded activation.
    Returns:
        A tensor.
    """

    max_value = constant_op.constant(max_value, x.dtype.base_dtype)
    neg = constant_op.constant(-1, x.dtype.base_dtype)
    x = clip_ops.clip_by_value(x, neg, max_value)

    return x


def DC_layers(DC_drop_value, strings, input_DC):

    conv1_DC = layers.Conv2D(
        100, kernel_size=(strings, 5), padding="same", activation="tanh"
    )(input_DC)
    batch1_DC = layers.BatchNormalization()(conv1_DC)
    pool1_DC = layers.MaxPooling2D(pool_size=(1, 2))(batch1_DC)
    drop1_DC = layers.Dropout(DC_drop_value)(pool1_DC)

    conv2_DC = layers.Conv2D(
        100, kernel_size=(strings, 7), padding="same", activation="relu"
    )(drop1_DC)
    batch2_DC = layers.BatchNormalization()(conv2_DC)
    drop2_DC = layers.Dropout(DC_drop_value)(batch2_DC)

    conv3_DC = layers.Conv2D(
        100, kernel_size=(strings, 7), padding="same", activation="relu"
    )(drop2_DC)
    batch3_DC = layers.BatchNormalization()(conv3_DC)
    drop3_DC = layers.Dropout(DC_drop_value)(batch3_DC)

    conv4_DC = layers.Conv2D(
        100, kernel_size=(strings, 3), padding="valid", activation="relu"
    )(drop3_DC)
    batch4_DC = layers.BatchNormalization()(conv4_DC)
    pool4_DC = layers.MaxPooling2D(pool_size=(1, 2))(batch4_DC)
    drop4_DC = layers.Dropout(DC_drop_value)(pool4_DC)

    conv5_DC = layers.Conv2D(
        100, kernel_size=(1, 7), padding="same", activation="relu"
    )(drop4_DC)
    batch5_DC = layers.BatchNormalization()(conv5_DC)
    drop5_DC = layers.Dropout(DC_drop_value)(batch5_DC)

    conv6_DC = layers.Conv2D(
        100, kernel_size=(1, 7), padding="same", activation="relu"
    )(drop5_DC)
    batch6_DC = layers.BatchNormalization()(conv6_DC)
    drop6_DC = layers.Dropout(DC_drop_value)(batch6_DC)

    conv7_DC = layers.Conv2D(
        100, kernel_size=(1, 1), padding="same", activation="relu"
    )(drop6_DC)
    batch7_DC = layers.BatchNormalization()(conv7_DC)
    drop7_DC = layers.Dropout(DC_drop_value)(batch7_DC)

    conv8_DC = layers.Conv2D(
        100, kernel_size=(1, 1), padding="same", activation="sigmoid"
    )(drop7_DC)
    batch8_DC = layers.BatchNormalization()(conv8_DC)
    drop8_DC = layers.Dropout(DC_drop_value)(batch8_DC)

    flat_DC = layers.Flatten()(drop8_DC)

    return flat_DC


def IC_layers(IC_drop_value, strings_IC, input_IC):

    conv1_IC = layers.Conv2D(
        100, kernel_size=(strings_IC, 5), padding="same", activation="tanh"
    )(input_IC)
    batch1_IC = layers.BatchNormalization()(conv1_IC)
    pool1_IC = layers.MaxPooling2D(pool_size=(1, 2))(batch1_IC)
    drop1_IC = layers.Dropout(IC_drop_value)(pool1_IC)

    conv2_IC = layers.Conv2D(
        100, kernel_size=(strings_IC, 7), padding="same", activation="relu"
    )(drop1_IC)
    batch2_IC = layers.BatchNormalization()(conv2_IC)
    drop2_IC = layers.Dropout(IC_drop_value)(batch2_IC)

    conv3_IC = layers.Conv2D(
        100, kernel_size=(strings_IC, 7), padding="same", activation="relu"
    )(drop2_IC)
    batch3_IC = layers.BatchNormalization()(conv3_IC)
    drop3_IC = layers.Dropout(IC_drop_value)(batch3_IC)

    conv4_IC = layers.Conv2D(
        100, kernel_size=(strings_IC, 3), padding="valid", activation="relu"
    )(drop3_IC)
    batch4_IC = layers.BatchNormalization()(conv4_IC)
    pool4_IC = layers.MaxPooling2D(pool_size=(1, 2))(batch4_IC)
    drop4_IC = layers.Dropout(IC_drop_value)(pool4_IC)

    conv5_IC = layers.Conv2D(
        100, kernel_size=(1, 7), padding="same", activation="relu"
    )(drop4_IC)
    batch5_IC = layers.BatchNormalization()(conv5_IC)
    drop5_IC = layers.Dropout(IC_drop_value)(batch5_IC)

    conv6_IC = layers.Conv2D(
        100, kernel_size=(1, 7), padding="same", activation="relu"
    )(drop5_IC)
    batch6_IC = layers.BatchNormalization()(conv6_IC)
    drop6_IC = layers.Dropout(IC_drop_value)(batch6_IC)

    conv7_IC = layers.Conv2D(
        100, kernel_size=(1, 1), padding="same", activation="relu"
    )(drop6_IC)
    batch7_IC = layers.BatchNormalization()(conv7_IC)
    drop7_IC = layers.Dropout(IC_drop_value)(batch7_IC)

    conv8_IC = layers.Conv2D(
        100, kernel_size=(1, 1), padding="same", activation="sigmoid"
    )(drop7_IC)
    batch8_IC = layers.BatchNormalization()(conv8_IC)
    drop8_IC = layers.Dropout(IC_drop_value)(batch8_IC)

    flat_IC = layers.Flatten()(drop8_IC)

    return flat_IC


def IC_layers_3D(IC_drop_value, strings_ICx, strings_ICy, input_IC):

    conv1_IC = layers.Conv3D(
        32, kernel_size=(3, 3, 3), padding="same", activation="tanh"
    )(input_IC)
    batch1_IC = layers.BatchNormalization()(conv1_IC)
    pool1_IC = layers.MaxPooling3D(pool_size=(1, 1, 2))(batch1_IC)
    drop1_IC = layers.SpatialDropout3D(IC_drop_value)(pool1_IC)

    conv2_IC = layers.Conv3D(
        32, kernel_size=(3, 3, 3), padding="same", activation="relu"
    )(drop1_IC)
    batch2_IC = layers.BatchNormalization()(conv2_IC)
    drop2_IC = layers.SpatialDropout3D(IC_drop_value)(batch2_IC)

    conv3_IC = layers.Conv3D(
        32, kernel_size=(3, 3, 3), padding="same", activation="relu"
    )(drop2_IC)
    batch3_IC = layers.BatchNormalization()(conv3_IC)
    drop3_IC = layers.SpatialDropout3D(IC_drop_value)(batch3_IC)

    conv4_IC = layers.Conv3D(
        64, kernel_size=(3, 3, 3), padding="valid", activation="relu"
    )(drop3_IC)
    batch4_IC = layers.BatchNormalization()(conv4_IC)
    pool4_IC = layers.MaxPooling3D(pool_size=(1, 1, 2))(batch4_IC)
    drop4_IC = layers.SpatialDropout3D(IC_drop_value)(pool4_IC)

    conv5_IC = layers.Conv3D(
        128, kernel_size=(1, 1, 7), padding="same", activation="relu"
    )(drop4_IC)
    batch5_IC = layers.BatchNormalization()(conv5_IC)
    drop5_IC = layers.SpatialDropout3D(IC_drop_value)(batch5_IC)

    conv6_IC = layers.Conv3D(
        128, kernel_size=(1, 1, 7), padding="same", activation="relu"
    )(drop5_IC)
    batch6_IC = layers.BatchNormalization()(conv6_IC)
    drop6_IC = layers.SpatialDropout3D(IC_drop_value)(batch6_IC)

    conv7_IC = layers.Conv3D(
        128, kernel_size=(1, 1, 1), padding="same", activation="relu"
    )(drop6_IC)
    batch7_IC = layers.BatchNormalization()(conv7_IC)
    drop7_IC = layers.SpatialDropout3D(IC_drop_value)(batch7_IC)

    conv8_IC = layers.Conv3D(
        128, kernel_size=(1, 1, 1), padding="same", activation="relu"
    )(drop7_IC)
    batch8_IC = layers.BatchNormalization()(conv8_IC)
    drop8_IC = layers.SpatialDropout3D(IC_drop_value)(batch8_IC)

    flat_IC = layers.Flatten()(drop8_IC)

    return flat_IC


def make_network_3D(
    X_DC,
    X_IC1,
    X_IC2,
    X_IC3,
    num_labels,
    DC_drop_value,
    IC_drop_value,
    connected_drop_value,
):

    # DEEP CORE #
    # print("Train Data DC", X_DC.shape)
    strings = X_DC.shape[1]
    dom_per_string = X_DC.shape[2]
    dom_variables = X_DC.shape[3]

    # Conv DC + batch normalization, later dropout and maxpooling
    input_DC = Input(shape=(strings, dom_per_string, dom_variables))
    flat_DC = DC_layers(DC_drop_value, strings, input_DC)

    # ICECUBE NEAR DEEPCORE #
    # print("Train Data IC", X_IC.shape)
    strings_ICx = X_IC1.shape[1]
    strings_ICy = X_IC1.shape[2]
    dom_per_string_IC = X_IC1.shape[3]
    dom_variables_IC = X_IC1.shape[4]

    # Conv DC + batch normalization, later dropout and maxpooling
    input_IC1 = Input(
        shape=(strings_ICx, strings_ICy, dom_per_string_IC, dom_variables_IC)
    )
    flat_IC1 = IC_layers_3D(IC_drop_value, strings_ICx, strings_ICy, input_IC1)

    input_IC2 = Input(
        shape=(strings_ICx, strings_ICy, dom_per_string_IC, dom_variables_IC)
    )
    flat_IC2 = IC_layers_3D(IC_drop_value, strings_ICx, strings_ICy, input_IC2)
    input_IC3 = Input(
        shape=(X_IC3.shape[1], X_IC3.shape[2], dom_per_string_IC, dom_variables_IC)
    )
    flat_IC3 = IC_layers_3D(IC_drop_value, X_IC3.shape[1], X_IC3.shape[2], input_IC3)

    # PUT TOGETHER #
    concatted = layers.concatenate([flat_DC, flat_IC1, flat_IC2, flat_IC3])

    full1 = layers.Dense(300, activation="relu")(concatted)
    batch1_full = layers.BatchNormalization()(full1)
    dropf = layers.Dropout(connected_drop_value)(batch1_full)
    output = layers.Dense(num_labels, activation="linear")(dropf)
    model_DC = Model(inputs=[input_DC, input_IC1, input_IC2, input_IC3], outputs=output)

    return model_DC


def make_network(
    X_DC,
    X_IC,
    num_labels,
    DC_drop_value,
    IC_drop_value,
    connected_drop_value,
    activation="linear",
    uncertainty=False,
):

    # DEEP CORE #
    # print("Train Data DC", X_DC.shape)
    strings = X_DC.shape[1]
    dom_per_string = X_DC.shape[2]
    dom_variables = X_DC.shape[3]

    # Conv DC + batch normalization, later dropout and maxpooling
    input_DC = Input(shape=(strings, dom_per_string, dom_variables))

    conv1_DC = layers.Conv2D(
        100, kernel_size=(strings, 5), padding="same", activation="tanh"
    )(input_DC)
    batch1_DC = layers.BatchNormalization()(conv1_DC)
    pool1_DC = layers.MaxPooling2D(pool_size=(1, 2))(batch1_DC)
    drop1_DC = layers.Dropout(DC_drop_value)(pool1_DC)

    conv2_DC = layers.Conv2D(
        100, kernel_size=(strings, 7), padding="same", activation="relu"
    )(drop1_DC)
    batch2_DC = layers.BatchNormalization()(conv2_DC)
    drop2_DC = layers.Dropout(DC_drop_value)(batch2_DC)

    conv3_DC = layers.Conv2D(
        100, kernel_size=(strings, 7), padding="same", activation="relu"
    )(drop2_DC)
    batch3_DC = layers.BatchNormalization()(conv3_DC)
    drop3_DC = layers.Dropout(DC_drop_value)(batch3_DC)

    conv4_DC = layers.Conv2D(
        100, kernel_size=(strings, 3), padding="valid", activation="relu"
    )(drop3_DC)
    batch4_DC = layers.BatchNormalization()(conv4_DC)
    pool4_DC = layers.MaxPooling2D(pool_size=(1, 2))(batch4_DC)
    drop4_DC = layers.Dropout(DC_drop_value)(pool4_DC)

    conv5_DC = layers.Conv2D(
        100, kernel_size=(1, 7), padding="same", activation="relu"
    )(drop4_DC)
    batch5_DC = layers.BatchNormalization()(conv5_DC)
    drop5_DC = layers.Dropout(DC_drop_value)(batch5_DC)

    conv6_DC = layers.Conv2D(
        100, kernel_size=(1, 7), padding="same", activation="relu"
    )(drop5_DC)
    batch6_DC = layers.BatchNormalization()(conv6_DC)
    drop6_DC = layers.Dropout(DC_drop_value)(batch6_DC)

    conv7_DC = layers.Conv2D(
        100, kernel_size=(1, 1), padding="same", activation="relu"
    )(drop6_DC)
    batch7_DC = layers.BatchNormalization()(conv7_DC)
    drop7_DC = layers.Dropout(DC_drop_value)(batch7_DC)

    conv8_DC = layers.Conv2D(
        100, kernel_size=(1, 1), padding="same", activation="sigmoid"
    )(drop7_DC)
    batch8_DC = layers.BatchNormalization()(conv8_DC)
    drop8_DC = layers.Dropout(DC_drop_value)(batch8_DC)

    flat_DC = layers.Flatten()(drop8_DC)

    # ICECUBE NEAR DEEPCORE #
    # print("Train Data IC", X_IC.shape)
    strings_IC = X_IC.shape[1]
    dom_per_string_IC = X_IC.shape[2]
    dom_variables_IC = X_IC.shape[3]

    # Conv DC + batch normalization, later dropout and maxpooling
    input_IC = Input(shape=(strings_IC, dom_per_string_IC, dom_variables_IC))

    conv1_IC = layers.Conv2D(
        100, kernel_size=(strings_IC, 5), padding="same", activation="tanh"
    )(input_IC)
    batch1_IC = layers.BatchNormalization()(conv1_IC)
    pool1_IC = layers.MaxPooling2D(pool_size=(1, 2))(batch1_IC)
    drop1_IC = layers.Dropout(IC_drop_value)(pool1_IC)

    conv2_IC = layers.Conv2D(
        100, kernel_size=(strings_IC, 7), padding="same", activation="relu"
    )(drop1_IC)
    batch2_IC = layers.BatchNormalization()(conv2_IC)
    drop2_IC = layers.Dropout(IC_drop_value)(batch2_IC)

    conv3_IC = layers.Conv2D(
        100, kernel_size=(strings_IC, 7), padding="same", activation="relu"
    )(drop2_IC)
    batch3_IC = layers.BatchNormalization()(conv3_IC)
    drop3_IC = layers.Dropout(IC_drop_value)(batch3_IC)

    conv4_IC = layers.Conv2D(
        100, kernel_size=(strings_IC, 3), padding="valid", activation="relu"
    )(drop3_IC)
    batch4_IC = layers.BatchNormalization()(conv4_IC)
    pool4_IC = layers.MaxPooling2D(pool_size=(1, 2))(batch4_IC)
    drop4_IC = layers.Dropout(IC_drop_value)(pool4_IC)

    conv5_IC = layers.Conv2D(
        100, kernel_size=(1, 7), padding="same", activation="relu"
    )(drop4_IC)
    batch5_IC = layers.BatchNormalization()(conv5_IC)
    drop5_IC = layers.Dropout(IC_drop_value)(batch5_IC)

    conv6_IC = layers.Conv2D(
        100, kernel_size=(1, 7), padding="same", activation="relu"
    )(drop5_IC)
    batch6_IC = layers.BatchNormalization()(conv6_IC)
    drop6_IC = layers.Dropout(IC_drop_value)(batch6_IC)

    conv7_IC = layers.Conv2D(
        100, kernel_size=(1, 1), padding="same", activation="relu"
    )(drop6_IC)
    batch7_IC = layers.BatchNormalization()(conv7_IC)
    drop7_IC = layers.Dropout(IC_drop_value)(batch7_IC)

    conv8_IC = layers.Conv2D(
        100, kernel_size=(1, 1), padding="same", activation="sigmoid"
    )(drop7_IC)
    batch8_IC = layers.BatchNormalization()(conv8_IC)
    drop8_IC = layers.Dropout(IC_drop_value)(batch8_IC)

    flat_IC = layers.Flatten()(drop8_IC)

    # PUT TOGETHER #
    concatted = layers.concatenate([flat_DC, flat_IC])

    full1 = layers.Dense(300, activation="relu")(concatted)
    batch1_full = layers.BatchNormalization()(full1)
    dropf = layers.Dropout(connected_drop_value)(batch1_full)
    if uncertainty is not True:
        output = layers.Dense(num_labels, activation=activation)(dropf)
    else:
        if num_labels >= 1:
            output1 = layers.Dense(1, activation="linear")(dropf)
            error1 = layers.Dense(1, activation="linear")(output1)
            output = layers.concatenate([output1, error1])
        if num_labels >= 2:
            output2 = layers.Dense(1, activation="linear")(dropf)
            error2 = layers.Dense(1, activation="linear")(output2)
            output = layers.concatenate([output1, error1, output2, error2])
        if num_labels >= 3:
            output3 = layers.Dense(1, activation="linear")(dropf)
            error3 = layers.Dense(1, activation="linear")(output3)
            output = layers.concatenate(
                [output1, error1, output2, error2, output3, error3]
            )
    model_DC = Model(inputs=[input_DC, input_IC], outputs=output)

    return model_DC


def make_network_DC(
    X_DC, num_labels, DC_drop_value, IC_drop_value, connected_drop_value
):

    # DEEP CORE #
    # print("Train Data DC", X_DC.shape)
    strings = X_DC.shape[1]
    dom_per_string = X_DC.shape[2]
    dom_variables = X_DC.shape[3]

    # Conv DC + batch normalization, later dropout and maxpooling
    input_DC = Input(shape=(strings, dom_per_string, dom_variables))

    conv1_DC = layers.Conv2D(
        100, kernel_size=(strings, 5), padding="same", activation="tanh"
    )(input_DC)
    batch1_DC = layers.BatchNormalization()(conv1_DC)
    pool1_DC = layers.MaxPooling2D(pool_size=(1, 2))(batch1_DC)
    drop1_DC = layers.Dropout(DC_drop_value)(pool1_DC)

    conv2_DC = layers.Conv2D(
        100, kernel_size=(strings, 7), padding="same", activation="relu"
    )(drop1_DC)
    batch2_DC = layers.BatchNormalization()(conv2_DC)
    drop2_DC = layers.Dropout(DC_drop_value)(batch2_DC)

    conv3_DC = layers.Conv2D(
        100, kernel_size=(strings, 7), padding="same", activation="relu"
    )(drop2_DC)
    batch3_DC = layers.BatchNormalization()(conv3_DC)
    drop3_DC = layers.Dropout(DC_drop_value)(batch3_DC)

    conv4_DC = layers.Conv2D(
        100, kernel_size=(strings, 3), padding="valid", activation="relu"
    )(drop3_DC)
    batch4_DC = layers.BatchNormalization()(conv4_DC)
    pool4_DC = layers.MaxPooling2D(pool_size=(1, 2))(batch4_DC)
    drop4_DC = layers.Dropout(DC_drop_value)(pool4_DC)

    conv5_DC = layers.Conv2D(
        100, kernel_size=(1, 7), padding="same", activation="relu"
    )(drop4_DC)
    batch5_DC = layers.BatchNormalization()(conv5_DC)
    drop5_DC = layers.Dropout(DC_drop_value)(batch5_DC)

    conv6_DC = layers.Conv2D(
        100, kernel_size=(1, 7), padding="same", activation="relu"
    )(drop5_DC)
    batch6_DC = layers.BatchNormalization()(conv6_DC)
    drop6_DC = layers.Dropout(DC_drop_value)(batch6_DC)

    conv7_DC = layers.Conv2D(
        100, kernel_size=(1, 1), padding="same", activation="relu"
    )(drop6_DC)
    batch7_DC = layers.BatchNormalization()(conv7_DC)
    drop7_DC = layers.Dropout(DC_drop_value)(batch7_DC)

    conv8_DC = layers.Conv2D(
        100, kernel_size=(1, 1), padding="same", activation="relu"
    )(drop7_DC)
    batch8_DC = layers.BatchNormalization()(conv8_DC)
    drop8_DC = layers.Dropout(DC_drop_value)(batch8_DC)

    flat_DC = layers.Flatten()(drop8_DC)

    # PUT TOGETHER #
    # concatted = concatenate([flat_DC, flat_IC])

    full1 = layers.Dense(300, activation="relu")(flat_DC)
    batch1_full = layers.BatchNormalization()(full1)
    dropf = layers.Dropout(connected_drop_value)(batch1_full)
    output = layers.Dense(num_labels, activation="tanh")(dropf)
    model_DC = Model(inputs=[input_DC], outputs=output)

    return model_DC
