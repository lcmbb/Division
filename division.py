def division(Division,divisor, decimal_places):
    """
     :param Division:被除数
    :param divisor:除数
    :param decimal_places:后几位小数
    :return:结果
    """
    import numpy as np
    go_num=1
    factor=1
    Ok=False
    while factor*divisor!=Division or  Ok==True:
        if factor*divisor==Division:
            pass

        elif factor*divisor>Division:
            factor-=go_num
            go_num=go_num/2
        else:
            factor+=go_num
        if factor//1!=factor:
            num = factor
            decimal_str = str(num).split('.')[1]
            decimal_len = len(decimal_str)  # 计算小数的位数
            if decimal_places>0:
                if decimal_len==decimal_places:
                    break

    return factor,decimal_places
