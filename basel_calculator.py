def calculate_car(tier1_capital, risk_weighted_assets):
    if risk_weighted_assets == 0:
        return 0
    return (tier1_capital / risk_weighted_assets) * 100

def calculate_lcr(hqla, net_outflows_30d):
    if net_outflows_30d == 0:
        return 0
    return (hqla / net_outflows_30d) * 100

def calculate_nsfr(asf, rsf):
    if rsf == 0:
        return 0
    return (asf / rsf) * 100
