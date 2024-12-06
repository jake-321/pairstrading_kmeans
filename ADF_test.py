import Kmeans_application as kk
import statsmodels.api as sm
import statsmodels.tsa.stattools as ts
import matplotlib.pyplot as plt

print(f'first pair {kk.pair_1}')
print(f'first pair {kk.pair_2}')

y1 = np.log(np.array(di.WMT)) #kk.pair_1[1]
x = np.log(np.array(di.NVDA)) #kk.pair_1[0]
x1 = sm.add_constant(x)

y2 = np.log(np.array(di.TGT)) #kk.pair_2[1]
x = np.log(np.array(di.AMZN)) #kk.pair_2[0]
x2 = sm.add_constant(x)

model = sm.OLS(y1,x1) #x2,y2
results = model.fit()
results.params

alpha = results.params[0]
beta = results.params[1]
x = np.squeeze(np.delete(x, 0,1))
error = y - (alpha + x* beta)

spread = error
z_score = (spread - np.mean(spread))/np.std(spread)

plt.figure(figsize= (12,6))
plt.plot(zscor, c = 'b')
plt.grid()
plt.axhline(-1.2, c = 'r')
plt.axhline(1.2, c= 'r')

test_statistic, p_val, _ = ts.coint(x,y)

print(f'test statistic: {test_statistic}')
print(f'p-value: {p_val}')