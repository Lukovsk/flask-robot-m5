extends Node2D


# Called when the node enters the scene tree for the first time.
func _ready():
	$Robozinho.rotate(50)

var speed = 3
# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	if Input.is_action_pressed("ui_right"):
		$Robozinho.position.x += speed
	if Input.is_action_pressed("ui_left"):
		$Robozinho.position.x -= speed
	if Input.is_action_pressed("ui_up"):
		$Robozinho.position.y -= speed
	if Input.is_action_pressed("ui_down"):
		$Robozinho.position.y += speed
	
	
	if Input.is_action_pressed("key_d"):
		$Robozinho2.position.x += speed
	if Input.is_action_pressed("key_a"):
		$Robozinho2.position.x -= speed
	if Input.is_action_pressed("key_w"):
		$Robozinho2.position.y -= speed
	if Input.is_action_pressed("key_s"):
		$Robozinho2.position.y += speed
