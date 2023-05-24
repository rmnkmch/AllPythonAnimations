from manim import *



class Example(Scene):
    def construct(self):
        UNKNOWN = "???"

        openingTextWriteTime = 0.9

        environmentCornerRadius = 0.1
        environmentOpacity = 0.2
        environmentWidth = 10
        environmentHeight = 7
        environmentHeightLittle = 3
        environmentTitleSize = 48

        channelMainSenseColor = GREEN
        principlesColor = BLUE
        symbolsColor = RED
        humanColor = ORANGE
        conceptColor = MAROON
        openedMenuColor = GRAY

        fadeScale = 0.1

        prVerticalOffset = 0.5 * DOWN
        prHorizontalOffset = 3.3 * RIGHT
        prUpRow = 2.44 * UP
        prMiddleRow = prUpRow + prVerticalOffset
        prDownRow = prUpRow + 2 * prVerticalOffset
        prLeftColumn = 3.3 * LEFT
        prRightColumn = prLeftColumn + 2 * prHorizontalOffset
        prShift1 = 0.3 * UP
        prStretchHeight1 = 2.2
        prShift2 = 5.2 * LEFT + 2.5 * UP
        prScale2 = 0.24

        menuPosition = 3.6 * UP + 6.4 * RIGHT

        prEnvCornerRadius = 1
        prEnvHeight = 3.1
        prEnvWidth = 5.6
        prDescrSize = 30
        prTitleSize = 40
        prMovedScale = 0.5
        prTitlePosition = UP
        prDescrPosition = 0.4 * DOWN
        prEnvHeight2 = 4.6
        prTitlePosition2 = 1.1 * UP
        prDescrPosition2 = 1.1 * DOWN
        prMovedScale2 = 0.4
        prCreatePosition2 = 1.48 * RIGHT + 1.1 * DOWN

        fundamentalSymbolScale = 0.17
        fundamentalSymbolOffset = 1.94 * RIGHT + 0.94 * UP
        fundamentalSymbolOffset2 = 2.06 * RIGHT + 1.63 * UP

        conceptTitleShift = 2.5 * RIGHT
        conceptDescrShift = 0.4 * UP
        conceptTitleSize = 50
        conceptDescrSize = 28
        conceptDescrPosition = 0.6 * DOWN

        humanPosition = DOWN
        humanCreatePosition = 2 * RIGHT + DOWN
        humanUpRow = 2.4 * UP
        humanDownRow = 1.2 * DOWN
        humanMiddleRow = 0.6 * UP
        humanLeftColumn = 3.2 * LEFT
        humanRightColumn = 3.2 * RIGHT
        humanInnerEnvScale = 0.7
        humPlusesPosition = 1.66 * UP
        humDotOffset = 3 * LEFT + 1.4 * UP
        humDotSize = 0.2

        indicateScale = 1.4
        spinInLagRatio = 0.28

        envCornerRadiusInMenu = 0.2
        envHeightInMenu = 1.3
        envWidthInMenu = 7.8
        textSizeInMenu = 32
        buffInMenu = 0.1
        upOffsetInMenu = -7.1
        menuClosedPosition = 11.5 * RIGHT
        menuOpenedPosition = 3.3 * RIGHT
        menuFadeTime = 0.3
        envTransformRunTime = 0.5
        envTransformScale = 0.04

        openingText = Text("Ну что ж ...")
        self.play(Write(openingText).set_run_time(openingTextWriteTime))
        self.play(
            Unwrite(openingText, reverse=False).set_run_time(openingTextWriteTime)
        )

        channelMainSenseEnv = RoundedRectangle(
            environmentCornerRadius,
            height=environmentHeightLittle,
            width=environmentWidth,
        ).set_fill(channelMainSenseColor, environmentOpacity)
        channelMainSenseTitle = Text(
            "Основной смысл канала", font_size=prTitleSize
        ).move_to(prTitlePosition)
        unknown = Text(UNKNOWN, font_size=prDescrSize, color=YELLOW).move_to(
            prDescrPosition
        )
        channelMainSenseDescr = unknown.copy()
        self.play(
            GrowFromCenter(channelMainSenseEnv, channelMainSenseColor),
            FadeIn(channelMainSenseTitle, scale=fadeScale, target_position=ORIGIN),
        )
        self.play(FadeIn(channelMainSenseDescr, scale=fadeScale))
        channelMainSenseG = Group(
            channelMainSenseEnv, channelMainSenseTitle, channelMainSenseDescr
        )

        menuDot1 = Dot(menuPosition, 0.03)
        menuDot2 = menuDot1.copy().move_to(menuPosition + 0.1 * DOWN)
        menuDot3 = menuDot1.copy().move_to(menuPosition + 0.2 * DOWN)
        menuLine1 = Line(menuPosition + 0.1 * RIGHT, menuPosition + 0.3 * RIGHT)
        menuLine2 = menuLine1.copy().move_to(menuPosition + 0.1 * DOWN + 0.2 * RIGHT)
        menuLine3 = menuLine1.copy().move_to(menuPosition + 0.2 * DOWN + 0.2 * RIGHT)
        menuG = Group(menuDot1, menuDot2, menuDot3, menuLine1, menuLine2, menuLine3)
        self.play(
            FadeOut(channelMainSenseG, scale=fadeScale, target_position=menuPosition),
            FadeIn(menuG, scale=fadeScale),
        )

        principlesEnv = RoundedRectangle(
            environmentCornerRadius, height=environmentHeight, width=environmentWidth
        ).set_fill(principlesColor, environmentOpacity)
        self.play(GrowFromCenter(principlesEnv, principlesColor))
        pr1Env = RoundedRectangle(
            prEnvCornerRadius, height=prEnvHeight, width=prEnvWidth
        )
        pr1Descr = Text("Все мы люди", font_size=prDescrSize)
        self.play(Create(pr1Env), FadeIn(pr1Descr))
        pr1G = Group(pr1Env, pr1Descr)
        self.play(pr1G.animate.move_to(prUpRow + prLeftColumn).scale(prMovedScale))
        pr2Env = RoundedRectangle(
            prEnvCornerRadius, height=prEnvHeight, width=prEnvWidth
        )
        pr2Descr = Text("Все люди\nхотят жить", font_size=prDescrSize)
        self.play(Create(pr2Env), FadeIn(pr2Descr))
        pr2G = Group(pr2Env, pr2Descr)
        self.play(pr2G.animate.move_to(prUpRow).scale(prMovedScale))
        pr3Env = RoundedRectangle(
            prEnvCornerRadius, height=prEnvHeight, width=prEnvWidth
        )
        pr3Descr = Text("Все люди\nхотят жить лучше", font_size=prDescrSize)
        self.play(Create(pr3Env), FadeIn(pr3Descr))
        pr3G = Group(pr3Env, pr3Descr)
        self.play(pr3G.animate.move_to(prUpRow + prRightColumn).scale(prMovedScale))
        prS = Group(pr1G, pr2G, pr3G)
        prUpRow += prShift1
        self.play(
            principlesEnv.animate.stretch_to_fit_height(prStretchHeight1).move_to(
                prUpRow
            ),
            prS.animate.move_to(prUpRow),
        )

        fundamentalSymbolTr1 = Triangle(color=YELLOW)
        fundamentalSymbolTr2 = (
            fundamentalSymbolTr1.copy().flip(LEFT).move_to(0.3 * DOWN)
        )
        fundamentalSymbol = Group(fundamentalSymbolTr1, fundamentalSymbolTr2)
        fundamentalSymbol1 = Group(
            fundamentalSymbolTr1.copy(), fundamentalSymbolTr2.copy()
        )
        fundamentalSymbol1.scale(fundamentalSymbolScale).move_to(
            prUpRow + prLeftColumn + fundamentalSymbolOffset * prMovedScale
        )
        fundamentalSymbol2 = Group(
            fundamentalSymbolTr1.copy(), fundamentalSymbolTr2.copy()
        )
        fundamentalSymbol2.scale(fundamentalSymbolScale).move_to(
            prUpRow + fundamentalSymbolOffset * prMovedScale
        )
        fundamentalSymbol3 = Group(
            fundamentalSymbolTr1.copy(), fundamentalSymbolTr2.copy()
        )
        fundamentalSymbol3.scale(fundamentalSymbolScale).move_to(
            prUpRow + prRightColumn + fundamentalSymbolOffset * prMovedScale
        )
        animG = AnimationGroup(
            SpinInFromNothing(fundamentalSymbol1),
            SpinInFromNothing(fundamentalSymbol2),
            SpinInFromNothing(fundamentalSymbol3),
            lag_ratio=spinInLagRatio,
        )
        symbolsEnv = RoundedRectangle(
            environmentCornerRadius, height=2.6, width=2.6
        ).set_fill(symbolsColor, environmentOpacity)
        self.play(GrowFromCenter(symbolsEnv, symbolsColor))
        self.play(SpinInFromNothing(fundamentalSymbol))
        symbolsDescr = Text("   -   фундаментальное", font_size=prDescrSize).move_to(
            RIGHT
        )
        self.play(
            symbolsEnv.animate.stretch_to_fit_width(8),
            fundamentalSymbol.animate.move_to(2.8 * LEFT),
            FadeIn(symbolsDescr, shift=1.7 * RIGHT),
        )
        self.play(animG)
        symbolsG = Group(fundamentalSymbol, symbolsEnv, symbolsDescr)
        self.play(FadeOut(symbolsG, scale=fadeScale, target_position=menuPosition))

        humanEnv = (
            RoundedRectangle(
                environmentCornerRadius, height=4.5, width=environmentWidth
            )
            .set_fill(humanColor, environmentOpacity)
            .move_to(humanPosition)
        )
        hum1 = RoundedRectangle(
            prEnvCornerRadius, height=prEnvHeight, width=prEnvWidth
        ).move_to(humanPosition)
        humanTitle = Text("Смысл жизни", font_size=prTitleSize).move_to(
            humanPosition + prTitlePosition
        )
        humanDecsr = Text("Жить лучше", font_size=prDescrSize).move_to(
            humanPosition + prDescrPosition
        )
        self.play(GrowFromCenter(humanEnv, humanColor))
        unknown.move_to(humanPosition + prDescrPosition)
        self.play(Create(hum1), FadeIn(humanTitle), FadeIn(unknown))
        self.play(
            FadeIn(humanDecsr, shift=conceptDescrShift),
            FadeOut(unknown, shift=conceptDescrShift),
        )
        hum1G = Group(hum1, humanTitle, humanDecsr)

        principlesG = Group(
            principlesEnv,
            prS,
            fundamentalSymbol1,
            fundamentalSymbol2,
            fundamentalSymbol3,
        )
        self.play(FadeOut(principlesG, scale=fadeScale, target_position=menuPosition))

        humanPosition = ORIGIN
        self.play(
            hum1G.animate.move_to(humanPosition + humanUpRow + humanLeftColumn).scale(
                prMovedScale
            ),
            humanEnv.animate.stretch_to_fit_height(environmentHeight).move_to(
                humanPosition
            ),
        )

        hum2 = RoundedRectangle(
            prEnvCornerRadius, height=prEnvHeight, width=prEnvWidth
        ).move_to(humanPosition + humanCreatePosition)
        humanTitle2 = Text("Человек", font_size=prTitleSize).move_to(
            humanPosition + humanCreatePosition + prTitlePosition
        )
        humanDescr2 = (
            Text("Самое\nсовершенное\nсущество", font_size=prDescrSize)
            .move_to(humanPosition + humanMiddleRow + humanLeftColumn + prDescrPosition)
            .scale(prMovedScale)
        )
        unknown.move_to(humanPosition + humanCreatePosition + prDescrPosition)
        hum2G = Group(hum2, humanTitle2, unknown)
        self.play(Create(hum2), FadeIn(humanTitle2), FadeIn(unknown))
        self.play(
            hum2G.animate.move_to(
                humanPosition + humanMiddleRow + humanLeftColumn
            ).scale(prMovedScale)
        )
        hum3 = RoundedRectangle(
            prEnvCornerRadius, height=prEnvHeight, width=prEnvWidth
        ).move_to(humanPosition + humanCreatePosition)
        humanTitle3 = Text("Достоинства:", font_size=prTitleSize).move_to(
            humanPosition + humanCreatePosition + prTitlePosition
        )
        hum3G = Group(hum3, humanTitle3)
        hum4 = RoundedRectangle(
            prEnvCornerRadius, height=prEnvHeight, width=prEnvWidth
        ).move_to(humanPosition + humanCreatePosition)
        humanTitle4 = Text("Недостатки:", font_size=prTitleSize).move_to(
            humanPosition + humanCreatePosition + prTitlePosition
        )
        hum4G = Group(hum4, humanTitle4)
        self.play(Create(hum3), FadeIn(humanTitle3, shift=conceptDescrShift))
        self.play(hum3G.animate.move_to(humanPosition + humanUpRow).scale(prMovedScale))
        self.play(Create(hum4), FadeIn(humanTitle4, shift=conceptDescrShift))
        self.play(
            hum4G.animate.move_to(humanPosition + humanUpRow + humanRightColumn).scale(
                prMovedScale
            )
        )
        self.play(
            FadeIn(humanDescr2, shift=conceptDescrShift),
            FadeOut(unknown, shift=conceptDescrShift),
        )
        hum2G = Group(hum2, humanTitle2, humanDescr2)

        self.play(
            hum3.animate.scale_to_fit_width(3)
            .stretch_to_fit_height(3)
            .move_to(humPlusesPosition)
        )

        unknown.move_to(prDescrPosition).scale(1 / prMovedScale)
        hum5 = RoundedRectangle(prEnvCornerRadius, height=prEnvHeight, width=prEnvWidth)
        humanTitle5 = Text("Разум", font_size=prTitleSize).move_to(prTitlePosition)
        humanDescr5 = unknown.copy()
        humanDot = Dot(humDotOffset, humDotSize)
        hum5G = (
            Group(hum5, humanTitle5, humanDot, humanDescr5)
            .scale(prMovedScale * humanInnerEnvScale)
            .move_to(humPlusesPosition)
        )

        self.play(
            AnimationGroup(
                Create(humanDot),
                Create(hum5),
                FadeIn(humanTitle5, scale=fadeScale, target_position=humanDot),
                FadeIn(humanDescr5, scale=fadeScale, target_position=humanTitle5),
                lag_ratio=0.3,
            )
        )
        humanG = Group(humanEnv, hum1G, hum2G, hum3G, hum4G, hum5G)
        self.play(FadeOut(humanG, scale=fadeScale, target_position=menuPosition))

        unknown.move_to(conceptDescrPosition)
        conceptEnv = RoundedRectangle(
            environmentCornerRadius,
            height=environmentHeightLittle,
            width=environmentWidth,
        ).set_fill(conceptColor, environmentOpacity)
        self.play(GrowFromCenter(conceptEnv, conceptColor))
        conceptTitle1 = Text("Совершенство", font_size=conceptTitleSize).move_to(
            prTitlePosition
        )
        conceptDescr1 = Text(
            "отсутствие недостатков", font_size=conceptDescrSize
        ).move_to(conceptDescrPosition)
        self.play(
            FadeIn(conceptTitle1, scale=fadeScale, shift=conceptTitleShift),
            FadeIn(unknown, scale=fadeScale, shift=conceptDescrShift),
        )
        self.play(
            FadeIn(conceptDescr1, shift=conceptDescrShift),
            FadeOut(unknown, shift=conceptDescrShift),
        )
        conceptTitle2 = Text("Разум", font_size=conceptTitleSize).move_to(
            prTitlePosition
        )
        self.play(
            FadeIn(conceptTitle2, shift=conceptTitleShift),
            FadeOut(conceptTitle1, shift=conceptTitleShift),
            FadeIn(unknown, shift=conceptDescrShift),
            FadeOut(conceptDescr1, shift=conceptDescrShift),
        )
        conceptDescr1 = Text("способность мыслить", font_size=conceptDescrSize).move_to(
            conceptDescrPosition
        )
        self.play(
            FadeIn(conceptDescr1, shift=conceptDescrShift),
            FadeOut(unknown, shift=conceptDescrShift),
        )
        conceptTitle1 = Text("Мышление", font_size=conceptTitleSize).move_to(
            prTitlePosition
        )
        self.play(
            FadeIn(conceptTitle1, shift=conceptTitleShift),
            FadeOut(conceptTitle2, shift=conceptTitleShift),
            FadeIn(unknown, shift=conceptDescrShift),
            FadeOut(conceptDescr1, shift=conceptDescrShift),
        )
        conceptDescr1 = Text(
            "познавательная деятельность", font_size=conceptDescrSize
        ).move_to(conceptDescrPosition)
        self.play(
            FadeIn(conceptDescr1, shift=conceptDescrShift),
            FadeOut(unknown, shift=conceptDescrShift),
        )
        conceptTitle2 = Text("Познание", font_size=conceptTitleSize).move_to(
            prTitlePosition
        )
        self.play(
            FadeIn(conceptTitle2, shift=conceptTitleShift),
            FadeOut(conceptTitle1, shift=conceptTitleShift),
            FadeIn(unknown, shift=conceptDescrShift),
            FadeOut(conceptDescr1, shift=conceptDescrShift),
        )
        conceptDescr1 = Text(
            "процесс приобретения знаний", font_size=conceptDescrSize
        ).move_to(conceptDescrPosition)
        self.play(
            FadeIn(conceptDescr1, shift=conceptDescrShift),
            FadeOut(unknown, shift=conceptDescrShift),
        )
        conceptTitle1 = Text("Знание", font_size=conceptTitleSize).move_to(
            prTitlePosition
        )
        self.play(
            FadeIn(conceptTitle1, shift=conceptTitleShift),
            FadeOut(conceptTitle2, shift=conceptTitleShift),
            FadeIn(unknown, shift=conceptDescrShift),
            FadeOut(conceptDescr1, shift=conceptDescrShift),
        )
        conceptDescr1 = Text(
            "совокупность некоторого количества фактов\nс известными взаимосвязями между ними",
            font_size=conceptDescrSize,
        ).move_to(conceptDescrPosition)
        self.play(
            FadeIn(conceptDescr1, shift=conceptDescrShift),
            FadeOut(unknown, shift=conceptDescrShift),
        )
        conceptTitle2 = Text("Факт", font_size=conceptTitleSize).move_to(
            prTitlePosition
        )
        self.play(
            FadeIn(conceptTitle2, shift=conceptTitleShift),
            FadeOut(conceptTitle1, shift=conceptTitleShift),
            FadeIn(unknown, shift=conceptDescrShift),
            FadeOut(conceptDescr1, shift=conceptDescrShift),
        )
        conceptDescr1 = Text(
            "отражение действительности\nв каком–то конкретном её проявлении",
            font_size=conceptDescrSize,
        ).move_to(conceptDescrPosition)
        self.play(
            FadeIn(conceptDescr1, shift=conceptDescrShift),
            FadeOut(unknown, shift=conceptDescrShift),
        )
        conceptTitle1 = Text("Действительность", font_size=conceptTitleSize).move_to(
            prTitlePosition
        )
        self.play(
            FadeIn(conceptTitle1, shift=conceptTitleShift),
            FadeOut(conceptTitle2, shift=conceptTitleShift),
            FadeIn(unknown, shift=conceptDescrShift),
            FadeOut(conceptDescr1, shift=conceptDescrShift),
        )
        conceptDescr1 = Text(
            "реальность во всей своей совокупности", font_size=conceptDescrSize
        ).move_to(conceptDescrPosition)
        self.play(
            FadeIn(conceptDescr1, shift=conceptDescrShift),
            FadeOut(unknown, shift=conceptDescrShift),
        )
        conceptG = Group(conceptEnv, conceptTitle1, conceptDescr1)
        self.play(FadeOut(conceptG, scale=fadeScale, target_position=menuPosition))

        openedMenuEnv = RoundedRectangle(0.06, height=8, width=8).set_fill(
            openedMenuColor, environmentOpacity
        )
        channelMainSenseEnvInMenu = RoundedRectangle(
            envCornerRadiusInMenu, height=envHeightInMenu, width=envWidthInMenu
        ).set_fill(channelMainSenseColor, environmentOpacity)
        channelMainSenseTextInMenu = Text(
            "Карта канала", font_size=textSizeInMenu
        ).move_to(channelMainSenseEnvInMenu)
        principlesEnvInMenu = RoundedRectangle(
            envCornerRadiusInMenu, height=envHeightInMenu, width=envWidthInMenu
        ).set_fill(principlesColor, environmentOpacity)
        principlesTextInMenu = Text(
            "Карта принципов", font_size=textSizeInMenu
        ).move_to(principlesEnvInMenu)
        symbolsEnvInMenu = RoundedRectangle(
            envCornerRadiusInMenu, height=envHeightInMenu, width=envWidthInMenu
        ).set_fill(symbolsColor, environmentOpacity)
        symbolsTextInMenu = Text(
            "Карта условных обозначений", font_size=textSizeInMenu
        ).move_to(symbolsEnvInMenu)
        humanEnvInMenu = RoundedRectangle(
            envCornerRadiusInMenu, height=envHeightInMenu, width=envWidthInMenu
        ).set_fill(humanColor, environmentOpacity)
        humanTextInMenu = Text("Карта человека", font_size=textSizeInMenu).move_to(
            humanEnvInMenu
        )
        conceptEnvInMenu = RoundedRectangle(
            envCornerRadiusInMenu, height=envHeightInMenu, width=envWidthInMenu
        ).set_fill(conceptColor, environmentOpacity)
        conceptTextInMenu = Text("Карта принципов", font_size=textSizeInMenu).move_to(
            conceptEnvInMenu
        )
        channelMainSenseInMenuG = Group(
            channelMainSenseEnvInMenu, channelMainSenseTextInMenu
        )
        principlesInMenuG = Group(principlesEnvInMenu, principlesTextInMenu)
        symbolsInMenuG = Group(symbolsEnvInMenu, symbolsTextInMenu)
        humanInMenuG = Group(humanEnvInMenu, humanTextInMenu)
        conceptInMenuG = Group(conceptEnvInMenu, conceptTextInMenu)
        allInMenuG = Group(
            channelMainSenseInMenuG,
            principlesInMenuG,
            symbolsInMenuG,
            humanInMenuG,
            conceptInMenuG,
        )
        allMenu = Group(
            openedMenuEnv,
            allInMenuG.arrange(DOWN, buffInMenu).next_to(
                openedMenuEnv, UP, upOffsetInMenu
            ),
        ).move_to(menuClosedPosition)

        self.play(Indicate(menuG, indicateScale))
        self.add(allMenu)
        self.play(
            FadeOut(menuG, scale=fadeScale).set_run_time(menuFadeTime),
            allMenu.animate.move_to(menuOpenedPosition),
        )
        self.play(Indicate(humanInMenuG))
        unchoosedG = Group(
            openedMenuEnv,
            channelMainSenseInMenuG,
            principlesInMenuG,
            symbolsInMenuG,
            conceptInMenuG,
        )
        self.play(
            unchoosedG.animate.move_to(menuClosedPosition),
            humanInMenuG.animate.move_to(humanPosition),
            FadeIn(menuG, scale=fadeScale),
        )
        self.play(
            FadeOut(humanInMenuG, scale=envTransformScale)
            .set_run_time(envTransformRunTime)
            .set_rate_func(ease_in_quad)
        )
        self.play(
            FadeIn(humanG, scale=envTransformScale)
            .set_run_time(envTransformRunTime)
            .set_rate_func(ease_out_quad)
        )

        self.play(hum4G.animate.move_to(humanPosition + humanDownRow + humanLeftColumn))
        humPlusesPosition += humanRightColumn / 3
        self.play(
            hum3.animate.stretch_to_fit_width(5.1).move_to(humPlusesPosition),
            hum5.animate.stretch_to_fit_width(3.9).move_to(humPlusesPosition),
            humanDescr5.animate.move_to(
                humPlusesPosition + prMovedScale * humanInnerEnvScale * prDescrPosition
            ),
        )

        humanDescr5Copy = (
            Text(
                "Cпособность находить\nзакономерности и взаимосвязи\nв окружающей действительности",
                font_size=prDescrSize,
            )
            .scale(prMovedScale * humanInnerEnvScale)
            .move_to(humPlusesPosition + humanInnerEnvScale * prDescrPosition)
        )
        self.play(
            FadeIn(humanDescr5Copy, shift=conceptDescrShift),
            FadeOut(humanDescr5, shift=conceptDescrShift),
        )
        humanDescr5 = humanDescr5Copy
        hum5G = Group(hum5, humanTitle5, humanDot, humanDescr5)
        humanG = Group(humanEnv, hum1G, hum2G, hum3G, hum4G, hum5G)
        self.play(FadeOut(humanG, scale=fadeScale, target_position=menuPosition))

        allMenu = Group(
            openedMenuEnv,
            allInMenuG.arrange(DOWN, buffInMenu).next_to(
                openedMenuEnv, UP, upOffsetInMenu
            ),
        ).move_to(menuClosedPosition)
        self.add(allMenu)
        self.play(Indicate(menuG, indicateScale))
        self.play(
            FadeOut(menuG, scale=fadeScale).set_run_time(menuFadeTime),
            allMenu.animate.move_to(menuOpenedPosition),
        )
        self.play(Indicate(channelMainSenseInMenuG))
        unchoosedG = Group(
            openedMenuEnv,
            principlesInMenuG,
            symbolsInMenuG,
            humanInMenuG,
            conceptInMenuG,
        )
        self.play(
            unchoosedG.animate.move_to(menuClosedPosition),
            channelMainSenseInMenuG.animate.move_to(ORIGIN),
            FadeIn(menuG, scale=fadeScale),
        )
        self.play(
            FadeOut(channelMainSenseInMenuG, scale=envTransformScale)
            .set_run_time(envTransformRunTime)
            .set_rate_func(ease_in_quad)
        )
        self.play(
            FadeIn(channelMainSenseG, scale=envTransformScale)
            .set_run_time(envTransformRunTime)
            .set_rate_func(ease_out_quad)
        )
        channelMainSenseDescrCopy = Text(
            "Улучшить жизнь человека\nпутём выявления законов мироздания",
            font_size=prDescrSize,
        ).move_to(prDescrPosition)
        self.play(
            FadeIn(channelMainSenseDescrCopy, shift=conceptDescrShift),
            FadeOut(channelMainSenseDescr, shift=conceptDescrShift),
        )
        channelMainSenseDescr = channelMainSenseDescrCopy
        channelMainSenseG = Group(
            channelMainSenseEnv, channelMainSenseTitle, channelMainSenseDescr
        )
        self.play(
            FadeOut(channelMainSenseG, scale=fadeScale, target_position=menuPosition)
        )

        allMenu = Group(
            openedMenuEnv,
            allInMenuG.arrange(DOWN, buffInMenu).next_to(
                openedMenuEnv, UP, upOffsetInMenu
            ),
        ).move_to(menuClosedPosition)
        self.add(allMenu)
        self.play(Indicate(menuG, indicateScale))
        self.play(
            FadeOut(menuG, scale=fadeScale).set_run_time(menuFadeTime),
            allMenu.animate.move_to(menuOpenedPosition),
        )
        self.play(Indicate(principlesInMenuG))
        unchoosedG = Group(
            openedMenuEnv,
            channelMainSenseInMenuG,
            symbolsInMenuG,
            humanInMenuG,
            conceptInMenuG,
        )
        self.play(
            unchoosedG.animate.move_to(menuClosedPosition),
            principlesInMenuG.animate.move_to(ORIGIN),
            FadeIn(menuG, scale=fadeScale),
        )
        self.play(
            FadeOut(principlesInMenuG, scale=envTransformScale)
            .set_run_time(envTransformRunTime)
            .set_rate_func(ease_in_quad)
        )
        self.play(
            FadeIn(principlesG, scale=envTransformScale)
            .set_run_time(envTransformRunTime)
            .set_rate_func(ease_out_quad)
        )

        prUpRow -= prShift1
        prS = Group(prS, fundamentalSymbol1, fundamentalSymbol2, fundamentalSymbol3)
        self.play(
            principlesEnv.animate.stretch_to_fit_height(environmentHeight).move_to(
                ORIGIN
            ),
            prS.animate.move_to(prUpRow),
        )

        unknown.move_to(prCreatePosition2 + prTitlePosition2)
        prMiddleRow += (
            (prEnvHeight2 * prMovedScale2 + prEnvHeight * prMovedScale) * DOWN / 2
        )
        prDownRow += (
            (3 * prEnvHeight2 * prMovedScale2 + prEnvHeight * prMovedScale) * DOWN / 2
        )
        pr4Env = RoundedRectangle(
            prEnvCornerRadius, height=prEnvHeight2, width=prEnvWidth
        )
        pr4Descr = Text(
            "Все люди разные,\nи у каждого\nсвои собственные\nвзгляды на мир",
            font_size=prDescrSize,
        ).move_to(prDescrPosition2)
        pr4Title = Text(
            "Принцип\nнеизбежного\nчеловеческого\nразличия", font_size=prTitleSize
        ).move_to(prTitlePosition2)
        pr4G = Group(pr4Env, pr4Descr, pr4Title).move_to(prCreatePosition2)
        self.play(Create(pr4Env), FadeIn(pr4Descr), FadeIn(unknown))
        self.play(
            FadeIn(pr4Title, shift=conceptDescrShift),
            FadeOut(unknown, shift=conceptDescrShift),
        )
        self.play(pr4G.animate.move_to(prMiddleRow + prLeftColumn).scale(prMovedScale2))

        pr5Env = RoundedRectangle(
            prEnvCornerRadius, height=prEnvHeight2, width=prEnvWidth
        )
        pr5Descr = Text(
            "Любую сущность\nможно рассматривать\nс различных\nточек зрения",
            font_size=prDescrSize,
        ).move_to(prDescrPosition2)
        pr5Title = Text("Принцип\nточки зрения", font_size=prTitleSize).move_to(
            prTitlePosition2
        )
        pr5G = Group(pr5Env, pr5Descr, pr5Title).move_to(prCreatePosition2)
        self.play(Create(pr5Env), FadeIn(pr5Descr), FadeIn(unknown))
        self.play(
            FadeIn(pr5Title, shift=conceptDescrShift),
            FadeOut(unknown, shift=conceptDescrShift),
        )
        self.play(pr5G.animate.move_to(prDownRow + prLeftColumn).scale(prMovedScale2))

        principlesG = Group(principlesG, pr4G, pr5G)
        self.play(principlesG.animate.scale(prScale2).move_to(prShift2))

        unknown.move_to(conceptDescrPosition)
        conceptEnv = RoundedRectangle(
            environmentCornerRadius,
            height=environmentHeightLittle,
            width=environmentWidth,
        ).set_fill(conceptColor, environmentOpacity)
        self.play(GrowFromCenter(conceptEnv, conceptColor))
        conceptTitle1 = Text("Сущность", font_size=conceptTitleSize).move_to(
            prTitlePosition
        )
        conceptDescr1 = Text(
            "поведение предмета,\nотличающее его от всех остальных",
            font_size=conceptDescrSize,
        ).move_to(conceptDescrPosition)
        self.play(
            FadeIn(conceptTitle1, scale=fadeScale, shift=conceptTitleShift),
            FadeIn(unknown, scale=fadeScale, shift=conceptDescrShift),
        )
        self.play(
            FadeIn(conceptDescr1, shift=conceptDescrShift),
            FadeOut(unknown, shift=conceptDescrShift),
        )
        conceptG = Group(conceptEnv, conceptTitle1, conceptDescr1)
        self.play(FadeOut(conceptG, scale=fadeScale, target_position=menuPosition))
        self.play(principlesG.animate.scale(1 / prScale2).move_to(ORIGIN))

        unknown.move_to(prCreatePosition2 + prTitlePosition2)
        pr6Env = RoundedRectangle(
            prEnvCornerRadius, height=prEnvHeight2, width=prEnvWidth
        )
        pr6Descr = Text("Человек несовершенен", font_size=prDescrSize).move_to(
            prDescrPosition
        )
        pr6Title = Text("Принцип\nнесовершенства", font_size=prTitleSize).move_to(
            prTitlePosition2
        )
        pr6G = Group(pr6Env, pr6Descr, pr6Title).move_to(prCreatePosition2)
        self.play(Create(pr6Env), FadeIn(pr6Descr), FadeIn(unknown))
        self.play(
            FadeIn(pr6Title, shift=conceptDescrShift),
            FadeOut(unknown, shift=conceptDescrShift),
        )
        self.play(pr6G.animate.move_to(prMiddleRow).scale(prMovedScale2))
        fundamentalSymbol4 = Group(
            fundamentalSymbolTr1.copy(), fundamentalSymbolTr2.copy()
        )
        fundamentalSymbol4.scale(fundamentalSymbolScale).move_to(
            prMiddleRow + prLeftColumn + fundamentalSymbolOffset2 * prMovedScale2
        )
        fundamentalSymbol5 = Group(
            fundamentalSymbolTr1.copy(), fundamentalSymbolTr2.copy()
        )
        fundamentalSymbol5.scale(fundamentalSymbolScale).move_to(
            prDownRow + prLeftColumn + fundamentalSymbolOffset2 * prMovedScale2
        )
        fundamentalSymbol6 = Group(
            fundamentalSymbolTr1.copy(), fundamentalSymbolTr2.copy()
        )
        fundamentalSymbol6.scale(fundamentalSymbolScale).move_to(
            prMiddleRow + fundamentalSymbolOffset2 * prMovedScale2
        )
        animG = AnimationGroup(
            SpinInFromNothing(fundamentalSymbol4),
            SpinInFromNothing(fundamentalSymbol5),
            SpinInFromNothing(fundamentalSymbol6),
            lag_ratio=spinInLagRatio,
        )
        self.play(animG)
        principlesG = Group(
            principlesG,
            pr6G,
            fundamentalSymbol4,
            fundamentalSymbol5,
            fundamentalSymbol6,
        )
        self.play(FadeOut(principlesG, scale=fadeScale, target_position=menuPosition))


def ease_in_quad(t: float) -> float:
    return t * t


def ease_out_quad(t: float) -> float:
    return 1 - (1 - t) * (1 - t)