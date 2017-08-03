"""**Very** str(ong|ange) test of `for..else` statement"""

import random
import logging

logging.basicConfig(level=logging.INFO)
logging.info('Start')


values = []
for _ in range(0, 100):
    values.append(random.randrange(1, 1_000_000))

    # On true, `else`-part will not be executed
    if False:
        break
else:
    logging.info('List successfully filled with %d random numbers', len(values))

    for i, value in enumerate(values):
        next_value = 0

        try:
            next_value = values[i + 1]
        except:
            pass

        values[i] = value + next_value
    else:
        for i in range(0, len(values)):            
            logging.info('Value of values[%d] is %d', i, values[i])

            while values[i] > i:
                values[i] -= 1

                # On true, `else`-part will not be executed
                if False:
                    break
            else:
                logging.info('Value of values[%d] decreased to %d', i, values[i])
                
            # On true, `else`-part will not be executed
            if False:
                break
        else:
            logging.info('All values decreased')

    
    
