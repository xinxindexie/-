class Settings(object):

    def __init__(self):

        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (255,255,255)
        self.ball_lastT = 0
        self.ball_interval = 500
        self.score = 0
        self.winScore = 5
        self.scale = 50
        self.title = "ball"

        self.begin_game_text = "开始游戏"
        self.begin_game_textSize = 100
        self.begin_game_textFont = "simsunnsimsun"
        self.begin_game_textColor = (255,0,0)
        self.begin_game_textBgColor = (0,255,255)
        self.begin_game_text_plant = "豪华无人机"
        self.begin_game_text_bucket = "精致小竹篮"
        self.begin_game_text_all = "双人豪华包"
        self.begin_game_text_number = 3
        # 字体太大页面放不下
        self.begin_game_textSize_choose = 44

        self.over_game_text = "恭喜你！胜利者！"
        self.over_game_textSize = 90
        self.over_game_textFont = "simsunnsimsun"
        self.over_game_textColor = (255, 0, 0)
        self.over_game_textBgColor = (0, 255, 255)

        self.begin_game_num = 0

        self.ship_up = 1
        self.ship_down = 1
        self.ship_left = 1
        self.ship_right = 1

        self.bullet = 1

        self.bucket_right = 1
        self.bucket_left = 1

        self.game_ship_UD = 50
        self.game_ship_LR = 50
        self.game_bucket_LR = 50