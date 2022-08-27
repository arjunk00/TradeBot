import statistics as st

niftybees = [0.053,0.1401,0.0399,0.0267,-0.0105,-0.0471,0.0001,-0.0242,0.1223,0.0421,0.0321,0.077,-0.0359,0.0022,0.0242,-0.0043,0.0727,0.0179,-0.0218,0.0624,-0.2934,0.2496,0.0817,0.2272,0.0502,0.0621,0.1264,-0.0081,0.0084,-0.1017,0.1053]
juniourbees = [0.0349,0.2226,0.0955,0.0398,0.0183,-0.0065,0.0177,-0.0587,0.0609,0.1023,-0.0674,0.1807,0.0472,0.0521,0.1247,-0.0733,-0.0081,-0.03,0.0333,0.0065,-0.0339,0.0067,0.0409,-0.2504,0.2458,0.0503,0.1942,0.0432,0.1104,0.0981,-0.0041,-0.0228,-0.1238,0.1325]

print(len(niftybees),len(juniourbees))

r = 0.0355580763
meannifty = sum(niftybees)/len(niftybees)
meanjunior = sum(juniourbees)/len(juniourbees)

varnifty = st.variance(niftybees)
varjuniour = st.variance(juniourbees)

r0 = 0.0139
print(meannifty,meanjunior)

kai = (((meannifty-r0)**2)/varnifty) + (((meanjunior-r0)**2)/varjuniour)

wnifty = (meannifty-r0)*(r-r0)/(kai*varnifty)
wjunior = (meanjunior-r0)*(r-r0)/(kai*varjuniour)
wfd = 1-(wnifty+wjunior)

vartotal = (wnifty**2)*varnifty + (wjunior**2)*varjuniour
stdtotal = (vartotal)**(0.5)
print("w1,w2,w3: ",wnifty,wjunior,wfd)
print("vartotal, stdtotal: ",vartotal,stdtotal)

