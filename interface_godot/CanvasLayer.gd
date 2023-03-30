extends CanvasLayer

var all_positions
var http_request = HTTPRequest.new()

func _ready():
	add_child(http_request)
	http_request.request_completed.connect(self._http_request_completed)
	http_request.request("http://127.0.0.1:5000/get_all_positions")



func _http_request_completed(result, response_code, headers, body):
	var json = JSON.new()
	json.parse(body.get_string_from_utf8())
	var response = json.get_data()
	print(response) # id, x, y, z, rotation
	
	for position in response:
		await get_tree().create_timer(0.5).timeout
		print(position)
		$Sprite2D.position.x = position[1]
		$Sprite2D.position.y = position[2]

		$Sprite2D.modulate.r = position[3]
		$Sprite2D.modulate.g = position[1]
		
		$Sprite2D.rotation = position[4]
	$Timer.start()

func _on_timer_timeout():
	$Timer.wait_time = 1
	http_request.request("http://127.0.0.1:5000/get_position")
