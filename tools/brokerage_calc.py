def stt(turnover, buyqty, sellqty):
    avgprice = turnover / (buyqty + sellqty)
    stt = avgprice * sellqty * 0.00025
    return stt


def brokerage(price, quantity):
    brokerage = min(0.0003 * price * quantity, 20)
    return brokerage


def transaction_charge(turnover):
    transaction_charge = 0.0000345 * (turnover)
    return transaction_charge


def gst(brokerage, transaction_charge):
    gst = 0.18 * (brokerage + transaction_charge)
    return gst


def sebi_charges(turnover):
    sebi_charges = 0.000001 * turnover
    return sebi_charges


def stamp_charges(first_order_value):
    stamp = 0.00003 * first_order_value
    return stamp


def brokerage_deductions(daytradesdf):
    total_deduction, total_brokerage = 0, 0
    df = daytradesdf
    # if(len(df.index)%2!=0):
    #     df = df.head(-1)
    # else:
    #     df = daytradesdf
    print(df)
    for i in range(0, len(df.index), 2):
        first_order = df.iloc[i].values
        last_order = df.iloc[i + 1].values
        first_order_value = first_order[3] * first_order[4]
        last_order_value = last_order[3] * last_order[4]
        buy_price = first_order[4]
        sell_price = last_order[4]
        buyqty = first_order[3]
        sellqty = last_order[3]
        turnover = first_order_value + last_order_value

        brokerage_till_now = brokerage(buy_price, buyqty) + brokerage(sell_price, sellqty)
        # print(brokerage_till_now)
        # print(stt(turnover, buyqty, sellqty))
        # print(transaction_charge(turnover))
        # print(gst(
        #     brokerage_till_now, transaction_charge(turnover)))
        # print(sebi_charges(turnover))
        # print(stamp_charges(first_order_value))
        total_brokerage += brokerage_till_now

        if first_order[2] == 'B':
            deduction = stt(turnover, buyqty, sellqty) + brokerage_till_now + transaction_charge(turnover) + gst(
                brokerage_till_now, transaction_charge(turnover)) + sebi_charges(turnover) + stamp_charges(
                first_order_value)
            total_deduction += deduction
        elif first_order[2] == 'S':
            deduction = brokerage_till_now + transaction_charge(turnover) + gst(
                brokerage_till_now, transaction_charge(turnover)) + sebi_charges(turnover)
            total_deduction += deduction

    return {'brokerage': total_brokerage, 'deduction': total_deduction}
