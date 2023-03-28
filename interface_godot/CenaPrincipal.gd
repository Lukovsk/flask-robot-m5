extends Node2D

var url = "https://localhost:5000"
func _ready():
	$HTTPRequest.connect("request_completed", self, "_on_request_completed")
	var coords = $HTTPRequest.request("GET", url)

func _on_request_completed(result, response_code, headers, body):
	var json = JSON.parse(body.get_string_from_utf8())
	print(json.result)
