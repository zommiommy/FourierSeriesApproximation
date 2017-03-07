
# Foruier Series Approximation for discrete time serires

Dependancy:


```python
import numpy as np
from scipy import linalg
```

this function will get the coefficent $a_n$ and $b_n$ to approximate a function in the form 

$$f(t) = \frac{a_0}{2} + \sum_{n = 1}^{N} \left [ a_n cos(nwt) + b_n sin(nwt) \right ]$$

or in the form of
$$ f(t) = \sum_{n = 1}^{N} c_n sin(nwt + \phi_n)$$

## Time series to approximate

![Image](https://github.com/zommiommy/FourierSeriesApproximation/blob/master/start.png?raw=true)

## Result

![Image](https://github.com/zommiommy/FourierSeriesApproximation/blob/master/result.png?raw=true)
