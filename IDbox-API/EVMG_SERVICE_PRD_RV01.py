# https://ptt-dev.idboxrt.com/api/
# https://ptt-dev.idboxrt.com/api/

from asyncio.windows_events import NULL
from datetime import datetime, timedelta
import requests
import json
import time
import pyodbc
import logging
import random
# time_now = datetime.now()
# date_log = time_now.strftime("%Y_%m_%d__%H_%M_%S")
# log_part = 'C:/IDBOX_API_LOG/get_logconfig_%s.log' % date_log
# logging.basicConfig(filename=log_part, encoding='utf-8')
# logging.info('%s Start Run Script At : %s'% (date_log, time_now))
# print(log_part)

# SQLEXPRESS

line_enable = True
line_token_admin = '3vo17pQBz7HDVDA4svTz5wYOUjiJZJ0RXO3z0rnmOFZ'
url_line = 'https://notify-api.line.me/api/notify'
token_line = '3vo17pQBz7HDVDA4svTz5wYOUjiJZJ0RXO3z0rnmOFZ'
headers_line = {
            'content-type':
            'application/x-www-form-urlencoded',
            'Authorization':'Bearer '+token_line
        }

def send_line(line_token, line_msg):
    url_line = 'https://notify-api.line.me/api/notify'
    if line_token:
        token_line = line_token
    else:
        token_line = '3vo17pQBz7HDVDA4svTz5wYOUjiJZJ0RXO3z0rnmOFZ'
    headers_line = {
            'content-type':
            'application/x-www-form-urlencoded',
            'Authorization':'Bearer '+token_line
    }

    try:
        r = requests.post(url_line, headers=headers_line , data = {'message':line_msg})
    except :
        print("send line err")
    else:
        print("** --------------------------- ** Send Line already")


def compare_tag_val_prd(tag_val, tag_h4_value, tag_h3_value, tag_h2_value, tag_h1_value, tag_l1_value, tag_l2_value, tag_l3_value, tag_l4_value):
    # print("------------------------------------------------------ ==> ", "compare_tag_val")
    SQLSERVER_ASP = '.\SQLEXPRESS'
    SQLDB_ASP = 'event_mgr'
    str_conn_asp = 'Driver={SQL Server};Server=%s;Database=%s;Trusted_Connection=no;uid=sa;pwd=1234;' %(SQLSERVER_ASP, SQLDB_ASP)
    conn_asp = pyodbc.connect(str_conn_asp)
    cursor_asp = conn_asp.cursor()
    tag_status = ''
    tag_status_id = ''
    # print("******************************")

    try:
        cursor_asp.execute('SELECT * FROM dbo.event_StateDisplay;')
    except pyodbc.OperationalError as err:
        print("err is : ", err)
        logging.error('sql error : %s' %err)
    except pyodbc.DataError as err:
        print("err is : ", err)
        logging.error('sql error : %s' %err)
    except pyodbc.IntegrityError as err:
        print("err is : ", err)
        logging.error('sql error : %s' %err)
    except pyodbc.ProgrammingError as err:
        print("err is : ", err)
        logging.error('sql error : %s' %err)
    except pyodbc.NotSupportedError as err:
        print("err is : ", err)
        logging.error('sql error : %s' %err)
    except pyodbc.DatabaseError as err:
        print("err is : ", err)
        logging.error('sql error : %s' %err)
    except pyodbc.Error as err:
        print("err is : ", err)
    else:
        rows = cursor_asp.fetchall()
        conn_asp.close()

        if rows:
            state_dis_psv_max = rows[7][1]
            state_dis_ow_max  = rows[5][1]
            state_dis_ocg_max = rows[3][1]
            state_dis_std_max = rows[1][1]
            state_dis_normal  = rows[0][1]
            state_dis_std_min = rows[2][1]
            state_dis_ocg_min = rows[4][1]
            state_dis_ow_min  = rows[6][1]
            state_dis_psv_min = rows[8][1]
            state_dis_tag_err = rows[9][1]

            state_dis_psv_max_id = rows[7][0]
            state_dis_ow_max_id  = rows[5][0]
            state_dis_ocg_max_id = rows[3][0]
            state_dis_std_max_id = rows[1][0]
            state_dis_normal_id  = rows[0][0]
            state_dis_std_min_id = rows[2][0]
            state_dis_ocg_min_id = rows[4][0]
            state_dis_ow_min_id  = rows[6][0]
            state_dis_psv_min_id = rows[8][0]
            state_dis_tag_err_id = rows[9][0]

    tag_status = ''
    tag_status_id = ''

    tag_status_id = state_dis_tag_err_id

    if type(tag_val) == int or type(tag_val) == float:
        # if compare_condition > 0:
        tag_status_id = state_dis_normal

        if (tag_h4_value is not None) and (tag_val >= tag_h4_value):
            tag_status_id = state_dis_psv_max_id
            # return tag_status_id
        elif (tag_h3_value is not None) and (tag_val >= tag_h3_value):
            tag_status_id = state_dis_ow_max_id
            # return tag_status_id
        elif (tag_h2_value is not None) and (tag_val >= tag_h2_value):
            tag_status_id = state_dis_ocg_max_id
            # return tag_status_id
        elif (tag_h1_value is not None) and (tag_val >= tag_h1_value):
            tag_status_id = state_dis_std_max_id
            # return tag_status_id

        elif (tag_l4_value is not None) and (tag_val <= tag_l4_value):
            tag_status_id = state_dis_psv_min_id
            # return tag_status_id
        elif (tag_l3_value is not None) and (tag_val <= tag_l3_value):
            tag_status_id = state_dis_ow_min_id
            # return tag_status_id
        elif (tag_l2_value is not None) and (tag_val <= tag_l2_value):
            tag_status_id = state_dis_ocg_min_id
            # return tag_status_id
        elif (tag_l1_value is not None) and (tag_val <= tag_l1_value):  
            tag_status_id = state_dis_std_min_id
            # return tag_status_id
        else:
            tag_status_id = state_dis_normal_id
            # return tag_status_id

    # print(' compare_tag_val(',
    #     tag_val, 
    #     ',',
    #     tag_h4_value,
    #     ',',
    #     tag_h3_value,
    #      ',',
    #     tag_h2_value,
    #     ',', 
    #     tag_h1_value,
    #     ',', 
    #     tag_l1_value,
    #     ',',
    #     tag_l2_value,
    #     ',',
    #     tag_l3_value,
    #     ',',
    #     tag_l4_value,
    #     ')', 'tag_status_id is ', tag_status_id)

    # with open('test_genevent_log.csv', 'a', newline='') as file:
    #     writer = csv.writer(file)
    #     writer.writerow([str(tag_val), str(tag_h4_value),  str(tag_h3_value),  str(tag_h2_value), str(tag_h1_value),  str(tag_l1_value),  \
    #         str(tag_l2_value),  str(tag_l3_value),  str(tag_l4_value), tag_status_id])
    return tag_status_id, tag_status_id



def compare_tag_val(tag_val, tag_h4_value, tag_h3_value, tag_h2_value, tag_h1_value, tag_l1_value, tag_l2_value, tag_l3_value, tag_l4_value):

    state_dis_psv_max = ''
    state_dis_ow_max  = ''
    state_dis_ocg_max = ''
    state_dis_std_max = ''
    state_dis_normal  = ''
    state_dis_std_min = ''
    state_dis_ocg_min = ''
    state_dis_ow_min  = ''
    state_dis_psv_min = ''
    state_dis_tag_err = ''

    print("------------------------------------------------------ ==> ", "insert_new_tag_event")

    if tag_val:
        # SQLEXPRESS
        SQLSERVER_ASP = '.\SQLEXPRESS'
        SQLDB_ASP = 'event_mgr'
        str_conn_asp = 'Driver={SQL Server};Server=%s;Database=%s;Trusted_Connection=no;uid=sa;pwd=1234;' %(SQLSERVER_ASP, SQLDB_ASP)
        conn_asp = pyodbc.connect(str_conn_asp)
        cursor_asp = conn_asp.cursor()
        tag_status = ''
        tad_status_id = ''
        print("******************************")
        try:
            cursor_asp.execute('SELECT * FROM dbo.event_StateDisplay;')
        except pyodbc.OperationalError as err:
            print("err is 1: ", err)
            logging.error('sql error : %s' %err)
        except pyodbc.DataError as err:
            print("err is 2: ", err)
            logging.error('sql error : %s' %err)
        except pyodbc.IntegrityError as err:
            print("err is 3: ", err)
            logging.error('sql error : %s' %err)
        except pyodbc.ProgrammingError as err:
            print("err is 4: ", err)
            logging.error('sql error : %s' %err)
        except pyodbc.NotSupportedError as err:
            print("err is 5: ", err)
            logging.error('sql error : %s' %err)
        except pyodbc.DatabaseError as err:
            print("err is 6: ", err)
            logging.error('sql error : %s' %err)
        except pyodbc.Error as err:
            print("err is 7: ", err)
        else:
            rows = cursor_asp.fetchall()
            # print(" ========== -> ","rows[0][8]"," ---> ", rows)
            conn_asp.close()
            if rows:

                state_dis_psv_max = rows[0][1]
                state_dis_ow_max  = rows[1][1]
                state_dis_ocg_max = rows[2][1]
                state_dis_std_max = rows[3][1]
                state_dis_normal  = rows[4][1]
                state_dis_std_min = rows[5][1]
                state_dis_ocg_min = rows[6][1]
                state_dis_ow_min  = rows[7][1]
                state_dis_psv_min = rows[8][1]
                state_dis_tag_err = rows[9][1]

                state_dis_psv_max_id = rows[0][0]
                state_dis_ow_max_id  = rows[1][0]
                state_dis_ocg_max_id = rows[2][0]
                state_dis_std_max_id = rows[3][0]
                state_dis_normal_id  = rows[4][0]
                state_dis_std_min_id = rows[5][0]
                state_dis_ocg_min_id = rows[6][0]
                state_dis_ow_min_id  = rows[7][0]
                state_dis_psv_min_id = rows[8][0]
                state_dis_tag_err_id = rows[9][0]

    if type(tag_val) == int or type(tag_val) == float or type(tag_val) == float:
        if (tag_val > tag_l1_value) and (tag_val < tag_h1_value):
            # print("val in range lv1 and hv1")
            tag_status = state_dis_normal
            tad_status_id = state_dis_normal_id
            return tag_status, tad_status_id
        else:
            if tag_val >= tag_h1_value:
                if (tag_val >= tag_h1_value) and (tag_val < tag_h2_value):
                    # print("val in range hv1 and hv2")
                    tag_status = state_dis_std_max
                    tad_status_id = state_dis_std_max_id
                    return tag_status, tad_status_id
                elif (tag_val >= tag_h2_value) and (tag_val < tag_h3_value):
                    # print("val in range hv2 and hv3")
                    tag_status = state_dis_ocg_max
                    tad_status_id = state_dis_ocg_max_id
                    return tag_status, tad_status_id
                elif (tag_val >= tag_h3_value) and (tag_val < tag_h4_value):
                    # print("val in range hv3 and hv4")
                    tag_status = state_dis_ow_max
                    tad_status_id = state_dis_ow_max_id
                    return tag_status, tad_status_id
                else:
                    # print("val more than or equ hv4")
                    tag_status = state_dis_psv_max
                    tad_status_id = state_dis_psv_max_id
                    return tag_status, tad_status_id
                # check high side
            else:
                if (tag_val <= tag_l1_value) and (tag_val > tag_l2_value):
                    # print("val in range lv1 and lv2")
                    tag_status = state_dis_std_min
                    tad_status_id = state_dis_std_min_id
                    return tag_status, tad_status_id
                elif (tag_val <= tag_l2_value) and (tag_val > tag_l3_value):
                    # print("val in range lv2 and lv3")
                    tag_status = state_dis_ocg_min
                    tad_status_id = state_dis_ocg_min_id
                    return tag_status, tad_status_id
                elif (tag_val <= tag_l3_value) and (tag_val > tag_l4_value):
                    # print("val in range lv3 and lv4")
                    tag_status = state_dis_ow_min
                    tad_status_id = state_dis_ow_min_id
                    return tag_status, tad_status_id
                else:
                    # print("val less than or equ lv4")
                    tag_status = state_dis_psv_min
                    tad_status_id = state_dis_psv_min_id
                    return tag_status, tad_status_id
        # print("Tag status is ", tag_status)
    else:
        tag_status = state_dis_tag_err
        tad_status_id = state_dis_tag_err_id
        return tag_status, tad_status_id

def Conv_dict(a):
    print("------------------------------------------------------ ==> ", "Conv_dict")
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct

def insert_tag_tase_table():
    print("------------------------------------------------------ ==> ", "insert_tag_tase_table")

    SQLSERVER_ASP = '.\SQLEXPRESS'
    SQLDB_ASP = 'test_db'
    str_conn_asp = 'Driver={SQL Server};Server=%s;Database=%s;Trusted_Connection=no;uid=sa;pwd=1234;' %(SQLSERVER_ASP, SQLDB_ASP)
    conn_asp = pyodbc.connect(str_conn_asp)
    cursor_asp = conn_asp.cursor()
    print("---------------------------------------------------------------------------------")
    while True:

        try:
            cursor_asp.execute('''
                    INSERT INTO dbo.tag_rt (tag_name, description, tag_value, status, time_stamp, get_tag_index)\
                    VALUES (?, ?, ?, ?, ?, ?)''', "A123","A012 description", 22.2, "LOW", 12-12-2020, 124)
        except pyodbc.OperationalError as err:
            print("err is 8: ", err)
            logging.error('sql error : %s' %err)
        except pyodbc.DataError as err:
            print("err is 9: ", err)
            logging.error('sql error : %s' %err)
        except pyodbc.IntegrityError as err:
            print("err is 10: ", err)
            logging.error('sql error : %s' %err)
        except pyodbc.ProgrammingError as err:
            print("err is 11: ", err)
            logging.error('sql error : %s' %err)
        except pyodbc.NotSupportedError as err:
            print("err is 12: ", err)
            logging.error('sql error : %s' %err)
        except pyodbc.DatabaseError as err:
            print("err is 13: ", err)
            logging.error('sql error : %s' %err)
        except pyodbc.Error as err:
            print("err is 14: ", err)
        else:
            conn_asp.commit()
            logging.info('sql insert complete')
            print("** --------------------------------------------------------------------------------- ** insert data to database already")
        print("---------------------------------------------------------------------------------")
        time.sleep(5)

def get_tag_config():
    print("------------------------------------------------------ ==> ", "get_tag_config")

    SQLSERVER_ASP = '.\SQLEXPRESS'
    SQLDB_ASP = 'event_mgr'
    str_conn_asp = 'Driver={SQL Server};Server=%s;Database=%s;Trusted_Connection=no;uid=sa;pwd=1234;' %(SQLSERVER_ASP, SQLDB_ASP)
    conn_asp = pyodbc.connect(str_conn_asp)
    cursor_asp = conn_asp.cursor()

    tag_name_list = []
    tag_logid_name_list = []
    tag_precision_list = []

    tag_range_low_lv1_list = []
    tag_range_low_lv2_list = []
    tag_range_low_lv3_list = []
    tag_range_low_lv4_list = []

    tag_range_high_lv1_list = []
    tag_range_high_lv2_list = []
    tag_range_high_lv3_list = []
    tag_range_high_lv4_list = []

    tag_name_dict={}
    tag_logid_name_dect={}
    tag_precision_dict={}

    tag_range_low_lv1_dict = {}
    tag_range_low_lv2_dict = {}
    tag_range_low_lv3_dict = {}
    tag_range_low_lv4_dict = {}

    tag_range_high_lv1_dict = {}
    tag_range_high_lv2_dict = {}
    tag_range_high_lv3_dict = {}
    tag_range_high_lv4_dict = {}

    # print("---------------------------------------------------------------------")
    time_now = datetime.now()
    try:
        cursor_asp.execute('''
        SELECT * FROM dbo.tag_event_conf 
        where ( (monitoring_enabled = 1) and (isRegister = 1) and process_tag is not null and ((DATEDIFF ( minute , lastmodify , ? ) > poll_freq) or (lastmodify is null)) )
        ''', time_now)
    except pyodbc.OperationalError as err:
        print("err is 14: ", err)
        logging.error('sql error : %s' %err)
    except pyodbc.DataError as err:
        print("err is 16: ", err)
        logging.error('sql error : %s' %err)
    except pyodbc.IntegrityError as err:
        print("err is 17: ", err)
        logging.error('sql error : %s' %err)
    except pyodbc.ProgrammingError as err:
        print("err is 18: ", err)
        logging.error('sql error : %s' %err)
    except pyodbc.NotSupportedError as err:
        print("err is 19: ", err)
        logging.error('sql error : %s' %err)
    except pyodbc.DatabaseError as err:
        print("err is 20: ", err)
        logging.error('sql error : %s' %err)
    except pyodbc.Error as err:
        print("err is 21: ", err)
    else:
        rows = cursor_asp.fetchall()
        if rows:
            for row in rows:
                if row[0] == None :
                    pass
                else:
                    # append tag list  tag_logid_name_list
                    # print('row[25] ', row[25])
                    # tag_precision_list
                    if not row[25]:
                        row[25] = 5
                        print('row[25] ', row[25])

                    if not row[38]:
                        row[38] = datetime.now()
                        print('row[25] ', row[38])

                    if not row[4]:
                        row[4] = 3
                        print('set defualt tag_precision to 3')

                    tag_logid_name_int = row[0]
                    tag_logid_name_list.append(tag_logid_name_int)

                    if not row[2]:
                        row[2] = 'New Tag' + str()

                    tag_name_str = str(row[30])
                    tag_name_list.append(str(row[30]))

                    time_next_sampling = row[38] + timedelta(hours=0, minutes=row[25], seconds=0)
                    time_get = time_next_sampling.strftime("%Y-%m-%d %H:%M:%S")

                    tag_name_list.append(time_get)

                    tag_logid_name_list.append(tag_name_str)

                    # print('tag_logid_name_list ', tag_logid_name_list)

                    tag_precision_list.append(tag_name_str)
                    tag_precision_list.append(row[4])

                    # print('tag row[30] ', row[30], 'row[38] ', row[38], ' next ', time_next_sampling)
                     
                    # append tag range

                    tag_range_low_lv1_list.append(tag_name_str)
                    tag_range_low_lv1_list.append(row[13])

                    tag_range_low_lv2_list.append(tag_name_str)
                    tag_range_low_lv2_list.append(row[14])

                    tag_range_low_lv3_list.append(tag_name_str)
                    tag_range_low_lv3_list.append(row[15])

                    tag_range_low_lv4_list.append(tag_name_str)
                    tag_range_low_lv4_list.append(row[16])

                    tag_range_high_lv1_list.append(tag_name_str)
                    tag_range_high_lv1_list.append(row[12])

                    tag_range_high_lv2_list.append(tag_name_str)
                    tag_range_high_lv2_list.append(row[11])

                    tag_range_high_lv3_list.append(tag_name_str)
                    tag_range_high_lv3_list.append(row[10])

                    tag_range_high_lv4_list.append(tag_name_str)
                    tag_range_high_lv4_list.append(row[9])

            print('tag_logid_name_list ', tag_logid_name_list)
            logging.info('sql select complete')
            print("**---------------------------------------------------------------------** select leaw naa")

    # print("---------------------------------------------------------------------")
    conn_asp.close()
    if tag_name_list:
        # conv tag list to dict
        tag_logid_name_dect = Conv_dict(tag_logid_name_list)

        tag_name_dict = Conv_dict(tag_name_list)

        tag_precision_dict = Conv_dict(tag_precision_list)

        tag_range_low_lv1_dict = Conv_dict(tag_range_low_lv1_list)
        tag_range_low_lv2_dict = Conv_dict(tag_range_low_lv2_list)
        tag_range_low_lv3_dict = Conv_dict(tag_range_low_lv3_list)
        tag_range_low_lv4_dict = Conv_dict(tag_range_low_lv4_list)

        tag_range_high_lv1_dict = Conv_dict(tag_range_high_lv1_list)
        tag_range_high_lv2_dict = Conv_dict(tag_range_high_lv2_list)
        tag_range_high_lv3_dict = Conv_dict(tag_range_high_lv3_list)
        tag_range_high_lv4_dict = Conv_dict(tag_range_high_lv4_list)

    return (tag_logid_name_dect, tag_name_dict, tag_precision_dict, tag_range_low_lv1_dict, tag_range_low_lv2_dict, tag_range_low_lv3_dict, tag_range_low_lv4_dict, \
            tag_range_high_lv1_dict, tag_range_high_lv2_dict, tag_range_high_lv3_dict, tag_range_high_lv4_dict)

def update_feld_next_samplingtime(tagdict):
    print("------------------------------------------------------ ==> ", "update_feld_next_samplingtime")
    
    if tagdict : 
        SQLSERVER_ASP = '.\SQLEXPRESS'
        SQLDB_ASP = 'event_mgr'
        str_conn_asp = 'Driver={SQL Server};Server=%s;Database=%s;Trusted_Connection=no;uid=sa;pwd=1234;' %(SQLSERVER_ASP, SQLDB_ASP)
        conn_asp = pyodbc.connect(str_conn_asp)
        cursor_asp = conn_asp.cursor()
        # print("---------------------------------------------------------------------")
        for tag in tagdict.keys():
            # time_now = datetime.now()
            # time_get = time_now.strftime("%Y-%m-%d %H:%M:%S")  dict_value.get(tag)
            time_next_sampling = tagdict.get(tag)
            print(tag)
            print(time_next_sampling)
            try:
                cursor_asp.execute(''' 
                UPDATE dbo.tag_event_conf SET 
                next_samplingtime=?
                WHERE logid =?''' 
                ,time_next_sampling, tag)
            except pyodbc.OperationalError as err:
                print("err is 22: ", err)
                logging.error('sql error : %s' %err)
            except pyodbc.DataError as err:
                print("err is 23: ", err)
                logging.error('sql error : %s' %err)
            except pyodbc.IntegrityError as err:
                print("err is 24: ", err)
                logging.error('sql error : %s' %err)
            except pyodbc.ProgrammingError as err:
                print("err is 25: ", err)
                logging.error('sql error : %s' %err)
            except pyodbc.NotSupportedError as err:
                print("err is 26: ", err)
                logging.error('sql error : %s' %err)
            except pyodbc.DatabaseError as err:
                print("err is 27: ", err)
                logging.error('sql error : %s' %err)
            except pyodbc.Error as err:
                print("err is 28: ", err)
            else:
                conn_asp.commit()
                logging.info('sql update complete')
                print("** --------------------------------------------------------------------------------- ** update data on database already")
                print("** --------------------------- ** next sampling ", time_next_sampling)
        # print("---------------------------------------------------------------------")
        conn_asp.close()
        return taglist

def update_feld_next_samplingtime_tagname(tagdict, tag_rt_dict, tag_rt_stm_dict, tag_status_dict, tag_precision_dict):
    #round(tag_rt_dict.get(tag_name), tag_precision_dict.get(tag_name))
    print("------------------------------------------------------ ==> ", "update_feld_next_samplingtime_tagname")

    if tagdict : 
        SQLSERVER_ASP = '.\SQLEXPRESS'
        SQLDB_ASP = 'event_mgr'
        str_conn_asp = 'Driver={SQL Server};Server=%s;Database=%s;Trusted_Connection=no;uid=sa;pwd=1234;' %(SQLSERVER_ASP, SQLDB_ASP)
        conn_asp = pyodbc.connect(str_conn_asp)
        cursor_asp = conn_asp.cursor()
        print("---------------------------------------------------------------------")
        # print(tagdict)
        for tag in tagdict.keys():
            time_now = datetime.now()
            time_get = time_now.strftime("%Y-%m-%d %H:%M:%S") 
            time_next_sampling = tagdict.get(tag)
            print(tag)
            # print(time_next_sampling)
            tag_posi = 0
            if tag_precision_dict.get(tag) is not None:
                tag_posi = tag_precision_dict.get(tag)

            if tag_rt_dict.get(tag) is not None:
                last_tag_value = round(tag_rt_dict.get(tag), tag_posi) #tag_rt_dict.get(tag)

            last_tag_tstmp = tag_rt_stm_dict.get(tag)
            last_tag_staus = tag_status_dict.get(tag)
            print('last_tag_staus : ' ,last_tag_staus)

            try:
                cursor_asp.execute(''' 
                UPDATE dbo.tag_event_conf SET 
                last_value=?,
                last_timestamp=?,
                monitoring_state = ?,
                lastmodify=?, 
                next_samplingtime=?
                WHERE tag_name =?''' 
                , last_tag_value, last_tag_tstmp, last_tag_staus, time_get, time_next_sampling, tag)
            except pyodbc.OperationalError as err:
                print("err is 29: ", err)
                logging.error('sql error : %s' %err)
            except pyodbc.DataError as err:
                print("err is 30: ", err)
                logging.error('sql error : %s' %err)
            except pyodbc.IntegrityError as err:
                print("err is 31: ", err)
                logging.error('sql error : %s' %err)
            except pyodbc.ProgrammingError as err:
                print("err is 32: ", err)
                logging.error('sql error : %s' %err)
            except pyodbc.NotSupportedError as err:
                print("err is 33: ", err)
                logging.error('sql error : %s' %err)
            except pyodbc.DatabaseError as err:
                print("err is 34: ", err)
                logging.error('sql error : %s' %err)
            except pyodbc.Error as err:
                print("err is 35: ", err)
            else:
                conn_asp.commit()
                logging.info('sql update complete')
                print("** --------------------------------------------------------------------------------- ** update leaw naa")
                print("** --------------------------- ** TAG ", tag, ' last_tag_value ', last_tag_value,  'last_tag_staus ', last_tag_staus)
                print("** --------------------------- ** next sampling ", time_next_sampling)
        print("---------------------------------------------------------------------")
        conn_asp.close()
        return taglist

#------------------------------------------------------------------------------------------------------------------------------------------#
def updat_db(tag_dict):
    print("------------------------------------------------------ ==> ", "updat_db")
    tag_str = ''
    for tag in tag_dict.keys():
        tag_str += str(tag) + ','
    print(tag_str[:-1])
    script_sql = '''SELECT * FROM dbo.tag_event_conf where logid in (%s)''' %tag_str[:-1]
    print('script_sql  is :', script_sql, 'tag_str is :', tag_str)
#------------------------------------------------------------------------------------------------------------------------------------------#

def get_token():
    print("------------------------------------------------------ ==> ", "get_token")
    token_str = ''
    # url_token = "https://ptt-dev.idboxrt.com/api/token"
    url_token = "http://asphere.trueddns.com:49313/api/token"
    payload_token = "grant_type=password&username=root&password=root!"
    headers_token = {
        'cookie': "__cfduid=d5df7fa290f8aa8399f41406756ef21441605173952",
        'Content-Type': "application/x-www-form-urlencoded"
    }
    # print("---------------------------------------------------------------------")
    print('start get token ')
    try:
        response = requests.request("GET", url_token, data=payload_token, headers=headers_token, timeout=60)
    except requests.ConnectionError:
        print('get token error ConnectionError')
    except requests.exceptions.HTTPError:
        print('get token error HTTPError')
    except requests.exceptions.Timeout:
        print('get token error Time Out')
    else:
        if response.status_code == 200:
            token_obj = response.json()
            # print(token_obj)
            token_str = token_obj["access_token"]
            print('get token successfully')
    return token_str

def get_tag_value(tag_name_list):
    print("------------------------------------------------------ ==> ", "get_tag_value")

    tag_value_list = []
    tag_timestamp_list = []
    tag_value_dict = {}
    tag_timestamp_dict = {}

    token_str = get_token()
    # url = "https://ptt-dev.idboxrt.com/api/v1/data/real-time/"
    url = "http://asphere.trueddns.com:49313/api/v1/data/real-time/"

    payload = ""
    headers = {
        'cookie': "__cfduid=d5df7fa290f8aa8399f41406756ef21441605173952",
        'Authorization': "Bearer " + token_str,
        'Security-Group': "1"
        }
    for tag in tag_name_list:
        url_get = url+tag
        try:
            response = requests.request("GET", url_get, data=payload, headers=headers, timeout=20)
        except requests.ConnectionError:
            print('get token error ConnectionError')
        except requests.exceptions.HTTPError:
            print('get token error HTTPError')
        except requests.exceptions.Timeout:
            print('get token error Time Out')
        else:
            if response.status_code == 200:
                tag_obj = response.json()
                tag_value_list.append(str(tag_obj['tag']))
                tag_value_list.append(tag_obj['value'])
                tag_timestamp_list.append(str(tag_obj['tag']))
                tag_timestamp_list.append(tag_obj['timestamp'])
                print("tag_value_list", tag_value_list)
                # PV_VL[tag_obj['tag']] = round(tag_obj['value'],2)   
                # PV_TM[tag_obj['tag']] = tag_obj['timestamp']
    print('---------------------------------------------------------------------------------')
    tag_value_dict = Conv_dict(tag_value_list)
    tag_timestamp_dict = Conv_dict(tag_timestamp_list)
    print("tag_value_dict", tag_value_dict, "tag_timestamp_dict", tag_timestamp_dict)

def compare_tag(tag_dict):
    print("------------------------------------------------------ ==> ", "compare_tag")
    pass
    # token = get_token()
    # print(token)

def get_tag_value_dict_sim(tag_name_dict):
    print("------------------------------------------------------ ==> ", "get_tag_value_dict_sim")

    tag_value_list = []
    tag_value_dict = {}
    tag_timestamp_list = []
    tag_timestamp_dict = {}

    for tag in tag_name_dict.keys():
        # print(tag, random.uniform(0.0, 100.0))

        time_now_rt = datetime.now()
        time_get_stm = time_now_rt.strftime("%Y-%m-%d %H:%M:%S")

        tag_value_list.append(str(tag))
        tag_value_list.append(round(random.uniform(0.0, 100.0),2))

        tag_timestamp_list.append(str(tag))
        tag_timestamp_list.append(time_get_stm)

    tag_value_dict = Conv_dict(tag_value_list)
    # print("tag_value_dict", tag_value_dict,)
    # print("tag_value_dict", tag_value_dict, "tag_timestamp_dict", tag_timestamp_dict)
    # return tag_value_dict
    # print('----------------------------------------------------------------------------------------------------')
    tag_value_dict = Conv_dict(tag_value_list)
    tag_timestamp_dict = Conv_dict(tag_timestamp_list)
    # print("tag_value_dict", tag_value_dict, "tag_timestamp_dict", tag_timestamp_dict)
    return (tag_value_dict, tag_timestamp_dict)

def get_tag_value_dict(tag_name_dict):
    print("------------------------------------------------------ ==> ", "get_tag_value_dict")

    tag_value_list = []
    tag_value_dict = {}
    tag_timestamp_list = []    
    tag_timestamp_dict = {}

    token_str = get_token()

    # asphere.trueddns.com:49313
    url = "http://asphere.trueddns.com:49313/api/v1/data/real-time/"

    payload = ""
    headers = {
        'cookie': "__cfduid=d5df7fa290f8aa8399f41406756ef21441605173952",
        'Authorization': "Bearer " + token_str,
        'Security-Group': "1"
        }

    for tag in tag_name_dict.keys():
        url_get = url+tag
        # print(url_get)
        try:
            response = requests.request("GET", url_get, data=payload, headers=headers, timeout=20)
        except requests.ConnectionError:
            print('get token error ConnectionError')
        except requests.exceptions.HTTPError:
            print('get token error HTTPError')
        except requests.exceptions.Timeout:
            print('get token error Time Out')
        else:
            print('get => ', url_get, ' response => ', response.status_code)
            if response.status_code == 200:
                tag_obj = response.json()
                tag_value_list.append(str(tag_obj['tag']))
                tag_value_list.append(tag_obj['value'])
                tag_timestamp_list.append(str(tag_obj['tag']))
                tag_timestamp_list.append(tag_obj['timestamp'])
    
    print('---------------------------------------------------------------------------------')
    tag_value_dict = Conv_dict(tag_value_list)
    tag_timestamp_dict = Conv_dict(tag_timestamp_list)
    print('---------------------------------------------------------------------------------')
    print('tag_value_dict  --> ',tag_value_dict)
    # print("tag_value_dict", tag_value_dict, "tag_timestamp_dict", tag_timestamp_dict)




    return (tag_value_dict, tag_timestamp_dict)

def update_data_to_eventlog_check_exit_state(tagdict):
    print("------------------------------------------------------ ==> ", "update_data_to_eventlog_check_exit_state")
    SQLSERVER_ASP = '.\SQLEXPRESS'
    SQLDB_ASP = 'event_mgr'
    str_conn_asp = 'Driver={SQL Server};Server=%s;Database=%s;Trusted_Connection=no;uid=sa;pwd=1234;' %(SQLSERVER_ASP, SQLDB_ASP)
    conn_asp = pyodbc.connect(str_conn_asp)
    cursor_asp = conn_asp.cursor()
    tag_name = 'A01'

    # print("-> ========== -> ","tagdict"," ", tagdict)
    tag_for_insert = []
    tag_for_update = []

    for tag in tagdict.keys():    
        try:
            cursor_asp.execute('SELECT tag_name, state_start, state_end, logid FROM dbo.tag_event_log WHERE tag_name =? AND state_end is Null;', tag)
        except pyodbc.OperationalError as err:
            print("err is 36: ", err)
            logging.error('sql error : %s' %err)
        except pyodbc.DataError as err:
            print("err is 37: ", err)
            logging.error('sql error : %s' %err)
        except pyodbc.IntegrityError as err:
            print("err is 38: ", err)
            logging.error('sql error : %s' %err)
        except pyodbc.ProgrammingError as err:
            print("err is 39: ", err)
            logging.error('sql error : %s' %err)
        except pyodbc.NotSupportedError as err:
            print("err is 40: ", err)
            logging.error('sql error : %s' %err)
        except pyodbc.DatabaseError as err:
            print("err is 41: ", err)
            logging.error('sql error : %s' %err)
        except pyodbc.Error as err:
            print("err is 42: ", err)
        else:
            rows = cursor_asp.fetchall()
            if rows:
                # print(" ========== -> ","rows"," ", rows)
                # print(" ========== -> ","rows"," Update Exit Event")
                tag_for_update.append(rows[0][0])
            else:
                # print(" ========== -> ","rows"," ", rows)
                # print(" ========== -> ","rows"," Insert New Event")
                tag_for_insert.append(tag)

    conn_asp.close()
    print(" ========== -> ","tag_for_update"," ", tag_for_update)
    print(" ========== -> ","tag_for_insert"," ", tag_for_insert)
    return (tag_for_update, tag_for_insert)

def update_tag_event(tag_name_list, tag_rt_dict, tag_rt_stm_dict, tag_status_dict, tag_status_id_dict, tag_precision_dict):
    print("------------------------------------------------------ ==> ", "update_tag_event")
    if tag_name_list:
        SQLSERVER_ASP = '.\SQLEXPRESS'
        SQLDB_ASP = 'event_mgr'
        str_conn_asp = 'Driver={SQL Server};Server=%s;Database=%s;Trusted_Connection=no;uid=sa;pwd=1234;' %(SQLSERVER_ASP, SQLDB_ASP)
        conn_asp = pyodbc.connect(str_conn_asp)
        cursor_asp = conn_asp.cursor()
        for tag_name in tag_name_list:
            print(" ========== -> ","tag_name"," ", tag_name)
            # print(" ========== -> ","tag_name"," Update Exit Event")
            # print(" ========== -> ","tag_rt_dict"," ", tag_rt_dict.get(tag_name))
            # print(" ========== -> ","tag_rt_stm_dict"," ", tag_rt_stm_dict.get(tag_name))
            # print(" ========== -> ","tag_status_dict"," ", tag_status_dict.get(tag_name))
            # print(" ========== -> ","tag_status_id_dict"," ", tag_status_id_dict.get(tag_name))
            monitoring_state = tag_status_dict.get(tag_name)
            last_value = round(tag_rt_dict.get(tag_name), tag_precision_dict.get(tag_name))
            last_timestamp = tag_rt_stm_dict.get(tag_name)
            state_event_id = tag_status_id_dict.get(tag_name)
            print("******************************")
            try:
                cursor_asp.execute('SELECT * FROM dbo.tag_event_log  WHERE tag_name =? AND state_end is Null;', tag_name)
            except pyodbc.OperationalError as err:
                print("err is 43: ", err)
                logging.error('sql error : %s' %err)
            except pyodbc.DataError as err:
                print("err is 44: ", err)
                logging.error('sql error : %s' %err)
            except pyodbc.IntegrityError as err:
                print("err is 45: ", err)
                logging.error('sql error : %s' %err)
            except pyodbc.ProgrammingError as err:
                print("err is 46: ", err)
                logging.error('sql error : %s' %err)
            except pyodbc.NotSupportedError as err:
                print("err is 47: ", err)
                logging.error('sql error : %s' %err)
            except pyodbc.DatabaseError as err:
                print("err is 48: ", err)
                logging.error('sql error : %s' %err)
            except pyodbc.Error as err:
                print("err is 49: ", err)
            else:
                rows = cursor_asp.fetchall()
                # print(" ========== -> ","rows"," ", rows)
                if rows:
                    data_old = rows[0]
                    monitoring_state_old = data_old[1]
                    time_now = datetime.now()
                    print(" ========== -> ","monitoring_state"," ", monitoring_state)
                    print(" ========== -> ","monitoring_state_old"," ", monitoring_state_old)
                    if monitoring_state == monitoring_state_old :
                        print('++++++++++++++++++++++++++++++++ update_data_to_eventlog |--> if monitoring_state == monitoring_state_old : true')
                        state_end=None
                        event_end=None
                        lastmodify=time_now
                        cursor_asp.execute(''' \
                        UPDATE dbo.tag_event_log SET \
                        monitoring_state=?,lastmodify=?,last_value=?,last_timestamp=?
                        WHERE tag_name =? AND state_end is Null''' \
                        ,monitoring_state, lastmodify, last_value, last_timestamp, tag_name)
                        conn_asp.commit()
                        # state_end=?,event_end=?,monitoring_state=?,lastmodify=?,last_value=?,last_timestamp=?
                    else:
                        print('++++++++++++++++++++++++++++++++ ++++++++++++++++++++++++++++++++ update_data_to_eventlog |--> if monitoring_state == monitoring_state_old : false')
                        state_end=monitoring_state
                        event_end=last_timestamp
                        lastmodify=time_now
                        cursor_asp.execute(''' \
                        UPDATE dbo.tag_event_log SET \
                        state_end=?,event_end=?,monitoring_state=?,lastmodify=?,last_value=?,last_timestamp=?, state_end_id=?
                        WHERE tag_name =? AND state_end is Null''' \
                        ,state_end, event_end, monitoring_state, lastmodify, last_value, last_timestamp,  state_event_id, tag_name)
                        conn_asp.commit() 

                    # if line_enable:
                    #     msg = "Event UPDATE for tag %s status %s time_stamp %s" %(tag_name, tag_status_dict.get(tag_name), tag_rt_stm_dict.get(tag_name))
                    #     try:
                    #         r = requests.post(url_line, headers=headers_line , data = {'message':msg})
                    #     except :
                    #         print("send line err")
                    #     else:
                    #         print("** --------------------------- ** Line at r ", r)
        conn_asp.close()

def send_mail(_tag_id, tag_name, area1, area2, area3, area4, _state_start_id):
    SQLSERVER = '.\SQLEXPRESS'
    SQLDB = 'event_mgr'
    str_conn = 'Driver={SQL Server};Server=%s;Database=%s;Trusted_Connection=no;uid=sa;pwd=1234;'%(SQLSERVER, SQLDB)
    conn = pyodbc.connect(str_conn)
    cursor = conn.cursor()

    desState = _state_start_id
    _Area1 = area1
    _Area2 = area2
    _Area3 = area3
    _Area4 = area4

    user_email = []

    sql_script = \
    '''
        SELECT	d.desState, d.Area1 AS desArea1, d.Area2 AS desArea2, d.Area3 AS desArea3, d.Area4 AS desArea4,
                d.RecordId as desId 
                ,m.RecordId as desMemberId 
                ,m.userId 
                ,(select [FullName] from event_user u where u.UserId=m.userId) as fullname
                ,(select [LastName] from event_user u where u.UserId=m.userId) as lastName
                ,(select [UserEmail] from event_user u where u.UserId=m.userId) as email
        FROM dbo.event_Destination AS d 
                left outer join [event_DestinationMember] AS m on d.RecordId=m.desId
        where desState = ? and d.area1 = ?  and d.area2 = ?  and d.area3 = ?  and d.area4 = ?  and m.RecordId is not null
    '''

    try:
        print('---------------------------------------------------------------------------------------------------')
        cursor.execute(sql_script, desState, _Area1, _Area2, _Area3, _Area4)
    except pyodbc.OperationalError as err:
        print("err is 50: ", err)
        logging.error('sql error : %s' %err)
    except pyodbc.DataError as err:
        print("err is 51: ", err)
        logging.error('sql error : %s' %err)
    except pyodbc.IntegrityError as err:
        print("err is 52: ", err)
        logging.error('sql error : %s' %err)
    except pyodbc.ProgrammingError as err:
        print("err is 53: ", err)
        logging.error('sql error : %s' %err)
    except pyodbc.NotSupportedError as err:
        print("err is 54: ", err)
        logging.error('sql error : %s' %err)
    except pyodbc.DatabaseError as err:
        print("err is 55: ", err)
        logging.error('sql error : %s' %err)
    except pyodbc.Error as err:
        print("err is 56: ", err)
    else:
        rows = cursor.fetchall()
        conn.close()
        if rows:
            for row in rows:

                if user_email == NULL:
                    null_email = ''
                    user_email.append(null_email)
                if user_email == None:
                    null_email = ''
                    user_email.append(null_email)
                else:
                    user_email.append(row)
                print(user_email)
    print('---------------------------------------------------------------------------------------------------\n')


    if line_enable:
        if user_email == NULL:
            user_email = ''
        if user_email == None:
            user_email = ''

        msg = "Event Insert for tag %s \nStatus %s \nTag id %s \nArea1 : %s \nArea2 : %s \nArea3 : %s \nArea4 : %s \nUser : %s" \
              %(tag_name, _state_start_id, _tag_id, area1, area2, area3, area4, user_email)
        
        send_line(None, msg)

    # if line_enable:
    #     msg = "Event Insert for tag %s \nStatus %s \nTag id %s \nArea1 : %s \nArea2 : %s \nArea3 : %s \nArea4 : %s \nUser : %s" \
    #           %(tag_name, _state_start_id, _tag_id, area1, area2, area3, area4, user_email)
    # try:
    #     r = requests.post(url_line, headers=headers_line , data = {'message':msg})
    # except :
    #     print("send line err")
    # else:
    #     print("** --------------------------- ** Line at r ", r)

    # .\SQLEXPRESS


def insert_new_tag_event(tag_name_list, tag_rt_dict, tag_rt_stm_dict, tag_status_dict, tag_status_id_dict, tag_precision_dict):
    print("------------------------------------------------------ ==> ", "insert_new_tag_event")
    if tag_name_list:
        SQLSERVER_ASP = '.\SQLEXPRESS'
        SQLDB_ASP = 'event_mgr'
        str_conn_asp = 'Driver={SQL Server};Server=%s;Database=%s;Trusted_Connection=no;uid=sa;pwd=1234;' %(SQLSERVER_ASP, SQLDB_ASP)
        conn_asp = pyodbc.connect(str_conn_asp)
        cursor_asp = conn_asp.cursor()
        for tag_name in tag_name_list:
            print(" ========== -> ","tag_name"," ", tag_name)
            # print(" ========== -> ","tag_name"," Update Exit Event")
            # print(" ========== -> ","tag_rt_dict"," ", tag_rt_dict.get(tag_name))
            # print(" ========== -> ","tag_rt_stm_dict"," ", tag_rt_stm_dict.get(tag_name))
            # print(" ========== -> ","tag_status_dict"," ", tag_status_dict.get(tag_name))
            # print(" ========== -> ","tag_status_id_dict"," ", tag_status_id_dict.get(tag_name))
            print("******************************")
            tag_now_status = tag_status_dict.get(tag_name)
            if tag_now_status != 'OK':
                try:
                    cursor_asp.execute('SELECT * FROM dbo.tag_event_conf WHERE tag_name =?;', tag_name)
                except pyodbc.OperationalError as err:
                    print("err is 57: ", err)
                    logging.error('sql error : %s' %err)
                except pyodbc.DataError as err:
                    print("err is 58: ", err)
                    logging.error('sql error : %s' %err)
                except pyodbc.IntegrityError as err:
                    print("err is 59: ", err)
                    logging.error('sql error : %s' %err)
                except pyodbc.ProgrammingError as err:
                    print("err is 62: ", err)
                    logging.error('sql error : %s' %err)
                except pyodbc.NotSupportedError as err:
                    print("err is 61: ", err)
                    logging.error('sql error : %s' %err)
                except pyodbc.DatabaseError as err:
                    print("err is 62: ", err)
                    logging.error('sql error : %s' %err)
                except pyodbc.Error as err:
                    print("err is 63: ", err)
                else:
                    rows = cursor_asp.fetchall()
                    if rows:
                        # print(" ========== -> ","rows[0][2]"," ---> ", rows[0][2])
                        # round(tag_rt_dict.get(tag_name), tag_precision_dict.get(tag_name))
                        for row in rows:
                            print(" ========== -> row[2] --> tag_name ","--->"," ", row[2])
                            _state_start = tag_status_dict.get(tag_name)
                            _event_start = tag_rt_stm_dict.get(tag_name)
                            _state_end = None
                            _event_end = None
                            _last_sendmail = None
                            _event_comment = None
                            _event_type = None
                            _tag_id = row[0]
                            _state_start_id = tag_status_id_dict.get(tag_name)
                            _state_end_id = None

                            _tag_name = row[2]
                            _uom = row[3]
                            _precision = row[4]
                            _area1 = row[5]
                            _area2 = row[6]
                            _area3 = row[7]
                            _area4 = row[8]
                            _range4_max = row[9]
                            _range3_max = row[10]
                            _range2_max = row[11]
                            _range1_max = row[12]
                            _range1_min = row[13]
                            _range2_min = row[14]
                            _range3_min = row[15]
                            _range4_min = row[16]
                            _range4_max_action = row[17]
                            _range3_max_action = row[18]
                            _range2_max_action = row[19]
                            _range1_max_action = row[20]
                            _range1_min_action = row[21]
                            _range2_min_action = row[22]
                            _range3_min_action = row[23]
                            _range4_min_action = row[24]
                            _poll_freq = row[25]
                            _variable_type = row[26]
                            _monitoring_enabled = row[27]
                            _monitoring_state = row[28]
                            _datasource = row[29]
                            _process_tag = row[30]
                            _email_notification_time = row[31]
                            _enable_email = row[32]
                            _logdatetime = datetime.now() #row[33]
                            _lastmodify = row[34]
                            _last_value = round(tag_rt_dict.get(tag_name), tag_precision_dict.get(tag_name)) #row[35]
                            _last_timestamp = row[36]
                            _error_messege = row[37]
                            _next_samplingtime = row[38]
                            _eventType = None

                            try:
                                cursor_asp.execute('''
                                INSERT INTO dbo.tag_event_log ( \
                                    state_start,event_start,state_end,event_end,last_sendmail,event_comment,event_type,tag_id,tag_name,uom,precision \
                                    ,area1,area2,area3,area4,range4_max,range3_max,range2_max,range1_max,range1_min,range2_min,range3_min,range4_min \
                                    ,range4_max_action,range3_max_action,range2_max_action,range1_max_action,range1_min_action,range2_min_action,range3_min_action \
                                    ,range4_min_action,poll_freq,variable_type,monitoring_enabled,monitoring_state,datasource,process_tag,email_notification_time \
                                    ,enable_email,logdatetime,lastmodify,last_value,last_timestamp,error_messege,next_samplingtime ,eventType, state_start_id, state_end_id) \
                                    VALUES  \
                                    ( \
                                        ?,?,?,?,?,?,?,?,?,? \
                                        ,?,?,?,?,?,?,?,?,?,? \
                                        ,?,?,?,?,?,?,?,?,?,? \
                                        ,?,?,?,?,?,?,?,?,?,? \
                                        ,?,?,?,?,?,?,?,? \
                                    )''' \
                                        , _state_start, _event_start, _state_end, _event_end, _last_sendmail, _event_comment, _event_type, _tag_id, _tag_name, _uom \
                                        , _precision, _area1, _area2, _area3, _area4, _range4_max, _range3_max, _range2_max, _range1_max, _range1_min \
                                        , _range2_min, _range3_min, _range4_min, _range4_max_action, _range3_max_action, _range2_max_action, _range1_max_action, _range1_min_action, _range2_min_action, _range3_min_action \
                                        , _range4_min_action, _poll_freq, _variable_type, _monitoring_enabled, _monitoring_state, _datasource, _process_tag, _email_notification_time, _enable_email, _logdatetime \
                                        , _lastmodify, _last_value, _last_timestamp, _error_messege, _next_samplingtime, _eventType, _state_start_id, _state_end_id)
                                        # _state_start_id = tag_status_id_dict.get(tag_name)
                                        # _state_end_id = None
                            except pyodbc.OperationalError as err:
                                print("err is 64: ", err)
                                logging.error('sql error : %s' %err)
                            except pyodbc.DataError as err:
                                print("err is 65: ", err)
                                logging.error('sql error : %s' %err)
                            except pyodbc.IntegrityError as err:
                                print("err is 66: ", err)
                                logging.error('sql error : %s' %err)
                            except pyodbc.ProgrammingError as err:
                                print("err is 67: ", err)
                                logging.error('sql error : %s' %err)
                            except pyodbc.NotSupportedError as err:
                                print("err is 68: ", err)
                                logging.error('sql error : %s' %err)
                            except pyodbc.DatabaseError as err:
                                print("err is 69: ", err)
                                logging.error('sql error : %s' %err)
                            except pyodbc.Error as err:
                                print("err is 70: ", err)
                            else:
                                conn_asp.commit()
                                print(" ========== -> ","SQL ==> conn_asp.commit()")


                                

                            send_mail(_tag_id, tag_name, _area1, _area2, _area3, _area4, _state_start_id)
                
            else:
                print(" ========== -> ","Tag Status is OK not Insert to Database")
        conn_asp.close()

#--------------------------------------------------------------------------------------------------------------#
taglist = []
tag_dict = {}
#--------------------------------------------------------------------------------------------------------------#
tag_status_list = []
tag_status_dict = {}
#--------------------------------------------------------------------------------------------------------------#
tag_status_id_list = []
tag_status_id_dict = {}
#--------------------------------------------------------------------------------------------------------------#

#--------------------------------------------------------------------------------------------------------------#
tag_name_dict={}
tag_rt_dict={}
tag_rt_stm_dict={}
#--------------------------------------------------------------------------------------------------------------#


while True:
    time.sleep(2)
    # time_now = datetime.now()
    # time_next_sampling = time_now + timedelta(hours=0, minutes=1, seconds=0)
    # time_get = time_next_sampling.strftime("%Y-%m-%d %H:%M:%S")
    # print('time_get is :', time_get)
    tag_id_name_dict, tag_name_dict, tag_precision_dict, tag_l1_dict, tag_l2_dict, tag_l3_dict, tag_l4_dict, \
    tag_h1_dict, tag_h2_dict, tag_h3_dict, tag_h4_dict = get_tag_config()

    # print('tag_id_name_dict    ', tag_id_name_dict)
    # print('tag_name_dict    ', tag_name_dict)
    # print('tag_precision_dict   ', tag_precision_dict)
    tag_status_str = ''
    tag_event_id = ''
    if tag_id_name_dict:

        # print('tag_name_dict', tag_name_dict)
        # for tag in tag_id_name_dict:

        # for tag in tag_id_name_dict.keys():
        #     print('TAG is :', tag_id_name_dict.get(tag))

        # for key, value in tag_id_name_dict.items():
        #     if value == 'None':
        #         value = 'New Tag'

        #     print('Tag ID :',key ,' Tag Name :', value)

        # tag_rt_dict, tag_rt_stm_dict = get_tag_value_dict_sim(tag_name_dict)

        print('TAG Get Value is :', tag_name_dict)
        tag_rt_dict, tag_rt_stm_dict = get_tag_value_dict(tag_name_dict)
        
        print('tag_rt_dict is :', tag_rt_dict)
        print('tag_rt_stm_dict is :', tag_rt_stm_dict)

        tag_l1_value = None
        tag_l2_value = None
        tag_l3_value = None
        tag_l4_value = None

        tag_h1_value = None
        tag_h2_value = None
        tag_h3_value = None
        tag_h4_value = None

        for tag in tag_rt_dict.keys():
            print('TAG is :', tag)
            if tag_precision_dict.get(tag) is not None:
                tag_precision = tag_precision_dict.get(tag)
            else:
                tag_precision = 0
            
            if tag_rt_dict.get(tag) is not None:
                tag_rt_value = round(tag_rt_dict.get(tag), tag_precision)
            else:
                tag_rt_value = None

            tag_ts_value = tag_rt_stm_dict.get(tag)
            
            if tag_l1_dict.get(tag) is not None:
                tag_l1_value = round(tag_l1_dict.get(tag), tag_precision)
            else:
                tag_l1_value = None

            if tag_l2_dict.get(tag) is not None:
                tag_l2_value = round(tag_l2_dict.get(tag), tag_precision)
            else:
                tag_l2_value = None

            if tag_l3_dict.get(tag) is not None:
                tag_l3_value = round(tag_l3_dict.get(tag), tag_precision)
            else:
                tag_l3_value = None

            if tag_l4_dict.get(tag) is not None:
                tag_l4_value = round(tag_l4_dict.get(tag), tag_precision)
            else:
                tag_l4_value = None

            if tag_h1_dict.get(tag) is not None:
                tag_h1_value = round(tag_h1_dict.get(tag), tag_precision)
            else:
                tag_h1_value = None

            if tag_h2_dict.get(tag) is not None:
                tag_h2_value = round(tag_h2_dict.get(tag), tag_precision)
            else:
                tag_h2_value = None

            if tag_h3_dict.get(tag) is not None:
                tag_h3_value = round(tag_h3_dict.get(tag), tag_precision)
            else:
                tag_h3_value = None

            if tag_h4_dict.get(tag) is not None:
                tag_h4_value = round(tag_h4_dict.get(tag), tag_precision)
            else:
                tag_h4_value = None






            # print("---------------------------------------------------------------------")
            # print('TAG is :', tag)
            # print("---------------------------------------------------------------------")
            # print('tag_rt_value is :', tag_rt_value)
            # print('tag_ts_value is :', tag_ts_value)
            # print("---------------------------------------------------------------------")
            # print('tag_l1_value is :', tag_l1_value)
            # print('tag_l2_value is :', tag_l2_value)
            # print('tag_l3_value is :', tag_l3_value)
            # print('tag_l4_value is :', tag_l4_value)
            # print("---------------------------------")
            # print('tag_h1_value is :', tag_h1_value)
            # print('tag_h2_value is :', tag_h2_value)
            # print('tag_h3_value is :', tag_h3_value)
            # print('tag_h4_value is :', tag_h4_value)
            # print("---------------------------------------------------------------------")

            if tag_rt_value:
                # tag_status_str, tag_event_id = compare_tag_val(tag_rt_value, tag_h4_value, tag_h3_value, tag_h2_value, tag_h1_value, tag_l1_value, tag_l2_value, tag_l3_value, tag_l4_value)
                tag_status_str, tag_event_id = compare_tag_val_prd(tag_rt_value, tag_h4_value, tag_h3_value, tag_h2_value, tag_h1_value, tag_l1_value, tag_l2_value, tag_l3_value, tag_l4_value)
                # print('tag ststus is : ', tag_status_str)
                tag_status_list.append(str(tag))
                tag_status_list.append(str(tag_status_str))

                tag_status_id_list.append(str(tag))
                tag_status_id_list.append(str(tag_event_id))

    # tag_status_list = [] tag_status_id_dict
    # tag_status_dict = {}
            # print("---------------------------")
#-----------------------------------------------------------------------------------------------------------------------------------------------
        tag_status_dict = Conv_dict(tag_status_list)
        tag_status_id_dict = Conv_dict(tag_status_id_list)
        
        if tag_name_dict and tag_rt_dict and tag_rt_stm_dict and tag_status_dict and tag_precision_dict:
            
            # print("------------------------------------------------------")
            # print('tag_name_dict is :', tag_name_dict)
            # print('tag_rt_dict is :', tag_rt_dict)
            # print('tag_rt_stm_dict is :', tag_rt_stm_dict)
            # print('tag_status_dict is :', tag_status_dict)
            # print('tag_status_id_dict is :', tag_status_id_dict)
            # print("------------------------------------------------------")

            update_feld_next_samplingtime_tagname(tag_name_dict, tag_rt_dict, tag_rt_stm_dict, tag_status_id_dict, tag_precision_dict)
            tag_for_update, tag_for_insert = update_data_to_eventlog_check_exit_state(tag_rt_dict)

            if(tag_for_update):
                update_tag_event(tag_for_update, tag_rt_dict, tag_rt_stm_dict, tag_status_dict, tag_status_id_dict, tag_precision_dict)

            if(tag_for_insert):
                insert_new_tag_event(tag_for_insert, tag_rt_dict, tag_rt_stm_dict, tag_status_dict, tag_status_id_dict, tag_precision_dict)
#-----------------------------------------------------------------------------------------------------------------------------------------------



