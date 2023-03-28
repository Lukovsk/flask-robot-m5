extends CanvasLayer

var all_positions

func _ready():
	$Timer.start()
	var http_request = HTTPRequest.new()
	add_child(http_request)
	http_request.request_completed.connect(self._http_request_completed)
	http_request.request("http://127.0.0.1:5000/get_position")



func _http_request_completed(result, response_code, headers, body):
	var json = JSON.new()
	json.parse(body.get_string_from_utf8())
	var response = json.get_data()
	print(response)
	all_positions = response
	
	$Sprite2D.position.x = response['x']
	$Sprite2D.position.y = response['y']
	#$Sprite2D.scale = response['z']
	$Sprite2D.rotation = response['rotation']

func _on_timer_timeout():
	#$HTTPRequest.request("https://7yc0jq-5000.csb.app/books")
	pass
