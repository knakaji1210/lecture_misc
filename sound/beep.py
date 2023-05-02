def beep(freq, dur=100):
    """
        ビープ音を鳴らす.
        @param freq 周波数
        @param dur  継続時間（ms）
    """

# Macの場合には、Macに標準インストールされたplayコマンドを使います.
    import os
    os.system('play -n synth %s sin %s' % (dur/1000, freq))

# そのままではNGだったので以下を参考にsoxをHomebrewでインストール
# https://teratail.com/questions/214355

# 2000Hzで500ms秒鳴らす
beep(523, 1000)