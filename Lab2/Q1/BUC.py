import sys
import pandas as pd
import numpy as np

ALL = -1
DEBUG = False

def read_data(filename):
    df = pd.read_csv(filename, sep = '\t')
    dims = df.shape[1] - 1
    return (df, dims)


def dump_input2(input):
    if DEBUG: 
        print("\n.. BUC_rec invoked on:")
        print(input)
        print("......................\n")


def project_data(input, d):
    return input.iloc[:, d]


def select_data(input, d, val):
    col_name = input.columns[d]
    return input[input[col_name] == val]


def remove_first_dim(input):
    return input.iloc[:, 1:]

def slice_data_dim0(input, v):
    df_temp = select_data(input, 0, v)
    return remove_first_dim(df_temp)

def output(val):
    print(f'\t{val}')


def buc_rec4(data, L, R, x, y, dic):

    dump_input2(data)
    dims = data.shape[1]

    if dims == 1:
        input_sum = sum(project_data(data, 0))
        dic[tuple(L)] = input_sum
        R.append(input_sum)


    else:
        dim0_vals = set(project_data(data, 0).values)



        for dim0_v in dim0_vals:

            if(data.shape[0] == x and data.shape[1] == y):
                L.append(str(dim0_v))

            else:
                L.append(str(dim0_v))
            sub_data = slice_data_dim0(data, dim0_v)
            buc_rec4(sub_data, L, R, x, y, dic)
            L.pop()
        
        
        
        sub_data = remove_first_dim(data)
        if(data.shape[0] == x and data.shape[1] == y):
            L.append('ALL')

        else:
            L.append('ALL')
        
        buc_rec4(sub_data,L, R, x ,y, dic)

        L.pop()


def BUC_V1():
    data, d= read_data('../asset/a_.txt')
    columns_list = list(data.columns.values)

    measure_list = columns_list[-1]
    columns_L = columns_list[: -1]
    
    
    (x, y) = data.shape
    L = []
    R = []
    dic = {}
    buc_rec4(data, L, R, x, y, dic)


    dic_List = []

    for i in range(len(columns_L)):
        l = []
        for j in dic:
            l.append(j[i])

        dic_temp = {}
        dic_temp[columns_L[i]] = l
        dic_List.append(dic_temp)


    dic_temp = {}
    l = []
    for j in dic:
        l.append(dic[j])

    dic_temp[measure_list] = l
    dic_List.append(dic_temp)
    

    a= dic_List[0]

    for i in range(1, len(dic_List)):
        a.update(dic_List[i])

    df = pd.DataFrame(a, dtype = 'int64')
    return df
