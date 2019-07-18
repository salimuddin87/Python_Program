import requests

def test_list_tasks():
	try:
		r = requests.get("http://127.0.0.1:5000/tasks")
		print r.json()
	except ValueError:
		print "ERROR: No JSON object could be decoded"

def test_get_task(task_id):
    r = requests.get("http://127.0.0.1:5000/tasks/%s" % task_id)
    if not r.ok:
    	print "ERROR: Info requested is not found"
    	return
    print r.json()

def test_create_task():
	try:
		payload = [("completed", "False"), ("task", "Another task")]
		#payload = {"completed": False, "task": "Another task"}
		r = requests.post("http://localhost:5000/tasks", data=payload)
	except ValueError:
		print "ERROR: No JSON object could be decoded"

def test_mark_task_completed(task_id):
	
	r = requests.post("http://127.0.0.1:5000/tasks/%s/completed" % task_id)
	if r.status_code == 404:
		print "ERROR: 404 not found"
	else:
		print "success"

def test_mark_task_incomplete(task_id):

	r = requests.post("http://127.0.0.1:5000/tasks/%s/incomplete" % task_id)
	if r.status_code == 404:
		print "ERROR: 404 not found"
	else:
		print "success"

def test_delete_task(task_id):
	r = requests.delete("http://127.0.0.1:5000/tasks/%s" % task_id)
	if r.status_code == 404:
		print "ERROR: 404 not found"
	else:
		print "success"

def test_modify_task(task_id):
	payload = {"completed": "True", "task":"modified task"}
	url = ("http://127.0.0.1:5000/tasks/%s" % task_id)
	r = requests.put(url, data=payload)
	print r.status_code
	print r.ok
	print r.json()

if __name__ == '__main__':
	status = True
	while status:
		print "0. Enter to quit "
		print "1. Enter to see list of tasks "
		print "2. Enter to see specific task "
		print "3. Enter to create new task "
		print "4. Enter to set completed "
		print "5. Enter to set incomplete "
		print "6. Enter to delete a data "
		print "7. Enter to modify a data "
		x = int(input("Enter an integer number "))
		if x == 0:
			status = False
		elif x == 1:
			test_list_tasks()
		elif x == 2:
			test_get_task('FD5uXaxk')
		elif x == 3:
			test_create_task()
		elif x == 4:
			test_mark_task_completed('aL54QelK')
		elif x == 5:
			test_mark_task_incomplete('aL54QelK')
		elif x == 6:
			test_delete_task('aL54QelK')
		elif x == 7:
			test_modify_task('FD5uXaxk')
		else:
			print "ERROR: invalid option entered"