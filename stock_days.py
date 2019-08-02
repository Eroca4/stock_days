
def stock_days(consumption, actual_stock):

	#Check the types of the passed args.
	#Consumption arg must be of type list. Preferably str to avoid problems with SKU's that starts with 0.

	if not isinstance(consumption, list):
		raise TypeError("consumption quantities must be in a list object")

	if not isinstance(actual_stock, int) and not isinstance(actual_stock, float):
		raise TypeError("actual_stock must be of type int | float")

	# Initialize a counter to track the number of blocks(each day of consumption)_
	# that we use before we reach the top of the stack(actual stock).

	days_tracker = 0

	# Initialize another variable to add the daily consumption on it to keep track
	# of the stack status.

	stack_value = 0

	# Iterate over the daily consumption quantity of the product until the cumulate
	# of it becomes greater or equal than the actual stock.

	for daily_consumption in consumption:
		# If the stack value is still under and the whole next daily consumption doesn't 
		# overflow the stack limit(actual_stock) then keep incrementing the counters
		if stack_value < actual_stock and stack_value + daily_consumption <= actual_stock:

			days_tracker += 1
			stack_value += daily_consumption

		elif stack_value < actual_stock and stack_value + daily_consumption > actual_stock:
			# We capture the difference between the stack_value and the actual stock to see
			# how much of the next daily_consumption value we can add to the days_tracker(float).
			float_part = (actual_stock - stack_value) / daily_consumption
			days_tracker += float_part
			stack_value += daily_consumption
			# Since this conditional captures the last block we can exit the for loop.
			break
	if stack_value < actual_stock:
		return "+" + str(days_tracker)
	else:
		return str(days_tracker)


		