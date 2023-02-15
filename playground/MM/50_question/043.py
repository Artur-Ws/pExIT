import matplotlib.pylab as plt
import math

# 1. O(1)
# 2. O(log(n))
# 3. O(n)
# 4. O(n * log(n))
# 5. O(n**2)
# 6. O(2**n)

seria0 = [1] * 10
seria1 = list(range(1,11))
seria2 = [math.log(x) for x in seria1]
seria3 = [math.log(x) * x for x in seria1]
seria4 = [x**2 for x in seria1]
seria5 = [2**x for x in seria1]

plt.plot(seria0, label="O(1)")
plt.plot(seria2, label="O(log(n))")
plt.plot(seria1, label="O(n)")
plt.plot(seria3, label="O(n * log(n))")
plt.plot(seria4, label="O(n**2)")
plt.plot(seria5, label="O(2**n)")

plt.legend()
plt.show()


