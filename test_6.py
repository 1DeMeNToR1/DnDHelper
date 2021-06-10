player.tab.actiondungeon_su_bestiary.setObjectName("actiondungeon_su_bestiary")
player.tab.actiontentaculus_ru_bestiary = QtWidgets.QAction(MainWindow)
player.tab.actiontentaculus_ru_bestiary.setObjectName("actiontentaculus_ru_bestiary")
player.tab.actiondungeon_su_magic_items = QtWidgets.QAction(MainWindow)
player.tab.actiondungeon_su_magic_items.setObjectName("actiondungeon_su_magic_items")
player.tab.actiontentaculus_ru_magic_items = QtWidgets.QAction(MainWindow)
player.tab.actiontentaculus_ru_magic_items.setObjectName("actiontentaculus_ru_magic_items")
player.tab.actiondungeon_su_normal_items = QtWidgets.QAction(MainWindow)
player.tab.actiondungeon_su_normal_items.setObjectName("actiondungeon_su_normal_items")
player.tab.actiondnd5_club_normal_items = QtWidgets.QAction(MainWindow)
player.tab.actiondnd5_club_normal_items.setObjectName("actiondnd5_club_normal_items")
player.tab.actiondungeon_su_magic = QtWidgets.QAction(MainWindow)
player.tab.actiondungeon_su_magic.setObjectName("actiondungeon_su_magic")
player.tab.actiontentaculus_ru_magic = QtWidgets.QAction(MainWindow)
player.tab.actiontentaculus_ru_magic.setObjectName("actiontentaculus_ru_magic")
player.tab.action1 = QtWidgets.QAction(MainWindow)
player.tab.action1.setObjectName("action1")
player.tab.character_menu.addAction(player.tab.add_character)
player.tab.character_menu.addAction(player.tab.load_character)
player.tab.character_menu.addAction(player.tab.save_character)
player.tab.book_menu.addAction(player.tab.master_book)
player.tab.book_menu.addAction(player.tab.study_book)
player.tab.name_generator.addAction(player.tab.actionAutoNAME_AutoREALM_name_generator)
player.tab.name_generator.addAction(player.tab.actiontentaculus_ru_name_generator)
player.tab.bandit_name_generator.addAction(player.tab.actionstormtower_ru_bandit_name_generator)
player.tab.harakter_generator.addAction(player.tab.actionrandomall_ru_harakter_generator)
player.tab.country_name_generator.addAction(player.tab.actionrandomall_ru_county_name_generator)
player.tab.instr_character.addAction(player.tab.name_generator.menuAction())
player.tab.instr_character.addAction(player.tab.bandit_name_generator.menuAction())
player.tab.instr_character.addAction(player.tab.harakter_generator.menuAction())
player.tab.instr_character.addAction(player.tab.country_name_generator.menuAction())
player.tab.instr_character.addAction(player.tab.actionrpgtinker_com_country_name_generator)
player.tab.home_generator.addAction(player.tab.actionstormtower_ru_home_generator)
player.tab.city_generator.addAction(player.tab.actionwatabou_itch_io_city_generator)
player.tab.make_location.addAction(player.tab.home_generator.menuAction())
player.tab.make_location.addAction(player.tab.city_generator.menuAction())
player.tab.make_location.addAction(player.tab.actionCampaign_Cartographer_3_CC3_city_generator)
player.tab.make_location.addAction(player.tab.actionAutoREALM_city_generator)
player.tab.make_location.addAction(player.tab.actionpyromancers_com_city_generator)
player.tab.instruments_menu.addAction(player.tab.instr_character.menuAction())
player.tab.instruments_menu.addAction(player.tab.make_location.menuAction())
player.tab.instruments_menu.addAction(player.tab.sounds)
player.tab.bestiary.addAction(player.tab.actiondungeon_su_bestiary)
player.tab.bestiary.addAction(player.tab.actiontentaculus_ru_bestiary)
player.tab.magic_items.addAction(player.tab.actiondungeon_su_magic_items)
player.tab.magic_items.addAction(player.tab.actiontentaculus_ru_magic_items)
player.tab.normal_items.addAction(player.tab.actiondungeon_su_normal_items)
player.tab.normal_items.addAction(player.tab.actiondnd5_club_normal_items)
player.tab.items.addAction(player.tab.magic_items.menuAction())
player.tab.items.addAction(player.tab.normal_items.menuAction())
player.tab.magic.addAction(player.tab.actiondungeon_su_magic)
player.tab.magic.addAction(player.tab.actiontentaculus_ru_magic)
player.tab.usefull_menu.addAction(player.tab.bestiary.menuAction())
player.tab.usefull_menu.addAction(player.tab.items.menuAction())
player.tab.usefull_menu.addAction(player.tab.magic.menuAction())
player.tab.cubes.addAction(player.tab.action1)
player.tab.menuBar.addAction(player.tab.character_menu.menuAction())
player.tab.menuBar.addAction(player.tab.book_menu.menuAction())
player.tab.menuBar.addAction(player.tab.instruments_menu.menuAction())
player.tab.menuBar.addAction(player.tab.usefull_menu.menuAction())
player.tab.menuBar.addAction(player.tab.cubes.menuAction())
player.tab.menuBar.addAction(player.tab.configs.menuAction())
player.tab.menuBar.addAction(player.tab.vk_group.menuAction())
player.tab.menuBar.addAction(player.tab.help.menuAction())

player.tab.retranslateUi(MainWindow)
player.tab.characters_tab.setCurrentIndex(0)
player.tab.caractersistics.setCurrentIndex(0)
player.tab.description_person.setCurrentIndex(0)
player.tab.magic_list.setCurrentIndex(6)
player.tab.much_inventories.setCurrentIndex(2)
player.tab.state_person.setCurrentIndex(1)
QtCore.QMetaObject.connectSlotsByName(MainWindow)


def retranslateUi(self, MainWindow):
_translate = QtCore.QCoreApplication.translate
MainWindow.setWindowTitle(_translate("MainWindow", "D&D Helper(alphatest 0.4)"))
player.tab.athletics_labl.setText(_translate("MainWindow", "Атлетика"))
player.tab.save_giving_labl.setText(_translate("MainWindow", "Спас.Бр."))
player.tab.mod_strong_labl.setText(_translate("MainWindow", "Модификатор:"))
player.tab.athletics_checkboxhaving.setText(_translate("MainWindow", "Владение"))
player.tab.znachenie_strong_labl.setText(_translate("MainWindow", "Значение:"))
player.tab.competention_athletics_checkbox.setText(_translate("MainWindow", "Компет."))
player.tab.save_giving_strong_checkboxhaving.setText(_translate("MainWindow", "Владение"))
player.tab.description_strong_labl.setText(_translate("MainWindow", "Сила определяет телесную мощь, атлетичность \n"
                                              "и ваши физические возможности. Обычно вы будете \n"
                                              "использовать силу что бы подниматься, прыгать,\n"
                                              "плавать, в рукопашной драке, выбивать двери,\n"
                                              "поднимать ворота и разрывать оковы.\n"
                                              "\n"
                                              "Любой персонаж предпочитающий рукопашные бои,\n"
                                              " может извлечь выгоду\n"
                                              "из высокого показателя силы. \n"
                                              "Таким образом бойцы, фехтовальщики \n"
                                              "и другие воины предпочитают высокие показатели\n"
                                              "силы."))
player.tab.caractersistics.setTabText(player.tab.caractersistics.indexOf(player.tab.characteristics_strong),
                _translate("MainWindow", "Сила"))
player.tab.save_giving_labl_2.setText(_translate("MainWindow", "Спас.Бр."))
player.tab.acrobatica_checkboxhaving.setText(_translate("MainWindow", "Владение"))
player.tab.lovk_ryk_labl.setText(_translate("MainWindow", "Ловкость\n"
                                    "рук"))
player.tab.save_giving_dexterity_checkboxhaving.setText(_translate("MainWindow", "Владение"))
player.tab.mod_strong_labl_2.setText(_translate("MainWindow", "Модификатор:"))
player.tab.stealth_labl.setText(_translate("MainWindow", "Скрытность"))
player.tab.acrobatica_labl.setText(_translate("MainWindow", "Акробатика"))
player.tab.acrobatica_checkbox.setText(_translate("MainWindow", "Компет."))
player.tab.znachenie_dexterity_labl.setText(_translate("MainWindow", "Значение:"))
player.tab.lovk_ryk_checkbox.setText(_translate("MainWindow", "Компет."))
player.tab.stealth_checkbox.setText(_translate("MainWindow", "Компет."))
player.tab.lovk_ryk_checkboxhaving.setText(_translate("MainWindow", "Владение"))
player.tab.stealth_checkboxhaving.setText(_translate("MainWindow", "Владение"))
player.tab.description_dexterity_labl.setText(_translate("MainWindow", "Ловкость определяет вашу физическую гибкость,\n"
                                                 "рефлексы и баланс. Обычно вы используете ловкость\n"
                                                 "для выполнения акробатических действий,\n"
                                                 "таких как удержание баланса при перемещении\n"
                                                 "по опасной поверхности, искривление вашего тела\n"
                                                 "при перемещении в узких пространствах,\n"
                                                 "поражение врага метательным снарядом или освобождение\n"
                                                 "из пут.\n"
                                                 "Разбойники и другие персонажи, носящие легкую броню,\n"
                                                 "предпочитают высокую ловкость, это помогает им\n"
                                                 "избежать вражеских атак. Персонаж может использовать\n"
                                                 "ловкость, когда атакует с лука, пращи\n"
                                                 "или метательного оружия.\n"
                                                 "Любой персонаж, желающий быстро реагировать\n"
                                                 "на опасность будет получать пользу от высокой ловкости."))
player.tab.caractersistics.setTabText(player.tab.caractersistics.indexOf(player.tab.characteristics_dexterity),
                _translate("MainWindow", "Ловкость"))
player.tab.save_giving_bodybuild_checkboxhaving.setText(_translate("MainWindow", "Владение"))
player.tab.znachenie_bodybuild_labl.setText(_translate("MainWindow", "Значение:"))
player.tab.save_giving_bodybuild_labl.setText(_translate("MainWindow", "Спас.Бр."))
player.tab.mod_bodybuild_labl.setText(_translate("MainWindow", "Модификатор:"))
player.tab.description_bodybuild_labl.setText(
_translate("MainWindow", "Телосложение определяет ваше здоровье и крепость.\n"
             "Обычно вы будете использовать телосложение что бы\n"
             "задерживать дыхание, совершать долгие походы,\n"
             "выполнять напряженную деятельность.\n"
             "\n"
             "Все персонажи получают выгоду\n"
             " от большого телосложения."))
player.tab.caractersistics.setTabText(player.tab.caractersistics.indexOf(player.tab.characteristics_bodybuild),
                _translate("MainWindow", "Телосложение"))
player.tab.mod_intellect_labl.setText(_translate("MainWindow", "Модификатор:"))
player.tab.analiz_checkboxhaving.setText(_translate("MainWindow", "Владение"))
player.tab.save_giving_intellect_labl.setText(_translate("MainWindow", "Спас.Бр."))
player.tab.religion_labl.setText(_translate("MainWindow", "Религия"))
player.tab.history_checkboxhaving.setText(_translate("MainWindow", "Владение"))
player.tab.history_labl.setText(_translate("MainWindow", "История"))
player.tab.history_checkbox.setText(_translate("MainWindow", "Компет."))
player.tab.magic_checkbox.setText(_translate("MainWindow", "Компет."))
player.tab.analiz_checkbox.setText(_translate("MainWindow", "Компет."))
player.tab.magic_checkboxhaving.setText(_translate("MainWindow", "Владение"))
player.tab.analiz_labl.setText(_translate("MainWindow", "Анализ"))
player.tab.save_giving_intellect_checkboxhaving.setText(_translate("MainWindow", "Владение"))
player.tab.nature_labl.setText(_translate("MainWindow", "Природа"))
player.tab.magic_labl.setText(_translate("MainWindow", "Магия"))
player.tab.znachenie_intellect_labl.setText(_translate("MainWindow", "Значение:"))
player.tab.nature_checkbox.setText(_translate("MainWindow", "Компет."))
player.tab.religion_checkbox.setText(_translate("MainWindow", "Компет."))
player.tab.nature_checkboxhaving.setText(_translate("MainWindow", "Владение"))
player.tab.religion_checkboxhaving.setText(_translate("MainWindow", "Владение"))
player.tab.description_intellect_labl.setText(_translate("MainWindow", "Интеллект описывает ваше психическое\n"
                                                 "видение мира, ваше образование,\n"
                                                 "способность к выявлению связей\n"
                                                 "причина-следствие, память и использование\n"
                                                 "логики для преодоления проблем и осложнений.\n"
                                                 "Обычно вы используете интеллект\n"
                                                 "для запоминания важных фактов,\n"
                                                 " нахождения ключей к головоломкам\n"
                                                 " или сотворения тайных заклинаний."))
player.tab.caractersistics.setTabText(player.tab.caractersistics.indexOf(player.tab.characteristics_intellect),
                _translate("MainWindow", "Интеллект"))
player.tab.mod_wise_labl.setText(_translate("MainWindow", "Модификатор:"))
player.tab.mindfulness_checkboxhaving.setText(_translate("MainWindow", "Владение"))
player.tab.save_giving_wise_labl.setText(_translate("MainWindow", "Спас.Бр."))
player.tab.care_of_animal_labl.setText(_translate("MainWindow", "Уход за\n"
                                          "живтными"))
player.tab.living_checkboxhaving.setText(_translate("MainWindow", "Владение"))
player.tab.living_labl.setText(_translate("MainWindow", "Выживание"))
player.tab.living_checkbox.setText(_translate("MainWindow", "Компет."))
player.tab.medicine_checkbox.setText(_translate("MainWindow", "Компет."))
player.tab.mindfulness_checkbox.setText(_translate("MainWindow", "Компет."))
player.tab.medicine_checkboxhaving.setText(_translate("MainWindow", "Владение"))
player.tab.mindfulness_labl.setText(_translate("MainWindow", "Вниматель-\n"
                                       "ность"))
player.tab.save_giving_wise_checkboxhaving.setText(_translate("MainWindow", "Владение"))
player.tab.insight_labl.setText(_translate("MainWindow", "Проница-\n"
                                   "тельность."))
player.tab.medicine_labl.setText(_translate("MainWindow", "Медицина"))
player.tab.znachenie_wise_labl.setText(_translate("MainWindow", "Значение:"))
player.tab.insight_checkbox.setText(_translate("MainWindow", "Компет."))
player.tab.care_of_animal_checkbox.setText(_translate("MainWindow", "Компет."))
player.tab.insight_checkboxhaving.setText(_translate("MainWindow", "Владение"))
player.tab.care_of_animal_checkboxhaving.setText(_translate("MainWindow", "Владение"))
player.tab.description_wise_labl.setText(_translate("MainWindow", "Мудрость отражает то,\n"
                                            "как вы приспособлены к своему\n"
                                            "окружению, представляет общую восприимчивость,\n"
                                            "интуицию, понимание и другие\n"
                                            "менее осязаемые чувства.\n"
                                            "\n"
                                            "Так же мудрость важна для понимания\n"
                                            "божественных указов и наставлений.\n"
                                            "Хотя мудрость является важным атрибутом\n"
                                            "для любого персонажа, который\n"
                                            "хочет быть внимательным, мудрость\n"
                                            "является особенно важной для жрецов и друидов,\n"
                                            "с помощью которой они могут направлять\n"
                                            "божественную силу и силы природы."))
player.tab.caractersistics.setTabText(player.tab.caractersistics.indexOf(player.tab.characteristics_wise),
                _translate("MainWindow", "Мудрость"))
player.tab.perfomance_checkboxhaving.setText(_translate("MainWindow", "Владение"))
player.tab.save_giving_charisma_labl.setText(_translate("MainWindow", "Спас.Бр."))
player.tab.bullying_checkboxhaving.setText(_translate("MainWindow", "Владение"))
player.tab.znachenie_charisma_labl.setText(_translate("MainWindow", "Значение:"))
player.tab.perfomance_checkbox.setText(_translate("MainWindow", "Компет."))
player.tab.fraud_checkbox.setText(_translate("MainWindow", "Компет."))
player.tab.save_giving_charisma_checkboxhaving.setText(_translate("MainWindow", "Владение"))
player.tab.fraud_checkboxhaving.setText(_translate("MainWindow", "Владение"))
player.tab.bullying_checkbox.setText(_translate("MainWindow", "Компет."))
player.tab.mod_charisma_labl.setText(_translate("MainWindow", "Модификатор:"))
player.tab.bullying_labl.setText(_translate("MainWindow", "Запугива-\n"
                                    "ние"))
player.tab.conviction_labl.setText(_translate("MainWindow", "Убежде-\n"
                                      "ние"))
player.tab.performance_labl.setText(_translate("MainWindow", "Выступле-\n"
                                       "ние"))
player.tab.fraud_labl.setText(_translate("MainWindow", "Обман"))
player.tab.conviction_checkbox.setText(_translate("MainWindow", "Компет."))
player.tab.conviction_checkboxhaving.setText(_translate("MainWindow", "Владение"))
player.tab.description_charisma_labl.setText(_translate("MainWindow", "Харизма определяет вашу способность\n"
                                                "влиять на других, и прочность вашей личности.\n"
                                                "Высокая харизма дает сильное чувство\n"
                                                "мотива, в то время как низкая\n"
                                                "харизма указывает на нестабильную личность.\n"
                                                "\n"
                                                "Харизма так же определяет насколько хорошим\n"
                                                "лидером вы можете быть.\n"
                                                "Все персонажи получают пользу\n"
                                                "от высокой харизмы, особенно те,\n"
                                                "кто имеет дело с НИП, приспешниками\n"
                                                "и умными монстрами. Так же харизма\n"
                                                "является важной характеристикой для тех,\n"
                                                "кто манипулирует магической мощью через\n"
                                                "чистую силу."))
player.tab.caractersistics.setTabText(player.tab.caractersistics.indexOf(player.tab.characteristics_charisma),
                _translate("MainWindow", "Харизма"))
player.tab.person_name.setText(_translate("MainWindow", "Абдулхабартат"))
player.tab.description_person.setItemText(player.tab.description_person.indexOf(player.tab.page_1),
                    _translate("MainWindow", "Черты характера и мировозрение"))
player.tab.description_person.setItemText(player.tab.description_person.indexOf(player.tab.page_2),
                    _translate("MainWindow", "Образ героя"))
player.tab.description_person.setItemText(player.tab.description_person.indexOf(player.tab.page_3),
                    _translate("MainWindow", "Идеалы"))
player.tab.description_person.setItemText(player.tab.description_person.indexOf(player.tab.page_4),
                    _translate("MainWindow", "Привязаности"))
player.tab.description_person.setItemText(player.tab.description_person.indexOf(player.tab.page_5),
                    _translate("MainWindow", "Слабости"))
player.tab.description_person.setItemText(player.tab.description_person.indexOf(player.tab.page_6),
                    _translate("MainWindow", "Предыстория"))
player.tab.description_person.setItemText(player.tab.description_person.indexOf(player.tab.page_7),
                    _translate("MainWindow", "Для заметок"))
player.tab.magic_list.setTabText(player.tab.magic_list.indexOf(player.tab.mag_lvl0), _translate("MainWindow", "Заговоры"))
player.tab.magic_list.setTabText(player.tab.magic_list.indexOf(player.tab.mag_lvl1), _translate("MainWindow", "1"))
player.tab.magic_list.setTabText(player.tab.magic_list.indexOf(player.tab.mag_lvl2), _translate("MainWindow", "2"))
player.tab.magic_list.setTabText(player.tab.magic_list.indexOf(player.tab.mag_lvl3), _translate("MainWindow", "3"))
player.tab.magic_list.setTabText(player.tab.magic_list.indexOf(player.tab.mag_lvl4), _translate("MainWindow", "4"))
player.tab.magic_list.setTabText(player.tab.magic_list.indexOf(player.tab.mag_lvl5), _translate("MainWindow", "5"))
player.tab.magic_list.setTabText(player.tab.magic_list.indexOf(player.tab.mag_lvl6), _translate("MainWindow", "6"))
player.tab.magic_list.setTabText(player.tab.magic_list.indexOf(player.tab.mag_lvl7), _translate("MainWindow", "7"))
player.tab.magic_list.setTabText(player.tab.magic_list.indexOf(player.tab.mag_lvl8), _translate("MainWindow", "8"))
player.tab.magic_list.setTabText(player.tab.magic_list.indexOf(player.tab.mag_lvl9), _translate("MainWindow", "9"))
player.tab.much_inventories.setTabText(player.tab.much_inventories.indexOf(player.tab.on_person_tab),
                 _translate("MainWindow", "Снаряжено"))
player.tab.much_inventories.setTabText(player.tab.much_inventories.indexOf(player.tab.inventory_tab),
                 _translate("MainWindow", "В инвент."))
player.tab.much_inventories.setTabText(player.tab.much_inventories.indexOf(player.tab.spechial_invent_tab),
                 _translate("MainWindow", "Спец.Предметы"))
player.tab.label_64.setText(_translate("MainWindow", "Класс:"))
player.tab.label_65.setText(_translate("MainWindow", "Уровень:"))
player.tab.label_66.setText(_translate("MainWindow", "Раса:"))
player.tab.label_68.setText(_translate("MainWindow", "Скорость:"))
player.tab.label_71.setText(_translate("MainWindow", "Кость хитов:"))
player.tab.up_character_checkbox.setText(_translate("MainWindow", "Вдохновление:"))
player.tab.label_73.setText(_translate("MainWindow", "Пас.Мудр\n"
                               "(вним.):"))
player.tab.label_47.setText(_translate("MainWindow", "Класс закл.:"))
player.tab.label_48.setText(_translate("MainWindow", "Базовая хар-ка:"))
player.tab.state_person.setTabText(player.tab.state_person.indexOf(player.tab_23), _translate("MainWindow", "Нету названия 2"))
player.tab.hp_labl.setText(_translate("MainWindow", "Здоровье:"))
player.tab.label_45.setText(_translate("MainWindow", "/"))
player.tab.initiative_labl.setText(_translate("MainWindow", "Инициатива:"))
player.tab.sl_spas_labl.setText(_translate("MainWindow", "Сл.Спасения:"))
player.tab.bon_attack_labl.setText(_translate("MainWindow", "Бон.Атаки:"))
player.tab.save_giving_of_death.setText(_translate("MainWindow", "Спас.Броски:"))
player.tab.save_giving_of_death_success.setText(_translate("MainWindow", "Успех:"))
player.tab.save_giving_of_death_fail.setText(_translate("MainWindow", "Провал:"))
player.tab.KD_labl.setText(_translate("MainWindow", "КД:"))
player.tab.xp_labl.setText(_translate("MainWindow", "Опыт:"))
player.tab.label_70.setText(_translate("MainWindow", "/"))
player.tab.bon_mast_labl.setText(_translate("MainWindow", "Бон.Маст:"))
player.tab.state_person.setTabText(player.tab.state_person.indexOf(player.tab_22), _translate("MainWindow", "Названия пока нету"))
player.tab.add_mag_button.setText(_translate("MainWindow", "Добавить"))
player.tab.red_view_mag_button.setText(_translate("MainWindow", "Редактировать/\n"
                                          "Просмотреть"))
player.tab.delete_mag_button.setText(_translate("MainWindow", "Удалить"))
player.tab.label_14.setText(_translate("MainWindow", "/"))
player.tab.label_9.setText(_translate("MainWindow", "8:"))
player.tab.label_5.setText(_translate("MainWindow", "4:"))
player.tab.label_10.setText(_translate("MainWindow", "9:"))
player.tab.label_6.setText(_translate("MainWindow", "5:"))
player.tab.label_16.setText(_translate("MainWindow", "/"))
player.tab.label_12.setText(_translate("MainWindow", "/"))
player.tab.label_7.setText(_translate("MainWindow", "6:"))
player.tab.label_2.setText(_translate("MainWindow", "2:"))
player.tab.label_3.setText(_translate("MainWindow", "/"))
player.tab.label_17.setText(_translate("MainWindow", "/"))
player.tab.label_4.setText(_translate("MainWindow", "3:"))
player.tab.label_13.setText(_translate("MainWindow", "/"))
player.tab.label_11.setText(_translate("MainWindow", "/"))
player.tab.label_15.setText(_translate("MainWindow", "/"))
player.tab.label_8.setText(_translate("MainWindow", "7:"))
player.tab.label_18.setText(_translate("MainWindow", "/"))
player.tab.label.setText(_translate("MainWindow", "1:"))
player.tab.label_19.setText(_translate("MainWindow", "0:"))
player.tab.Usefull_buttons.setTitle(_translate("MainWindow", "Полезные кнопки"))
player.tab.calculator_button.setText(_translate("MainWindow", "Калькулятор"))
player.tab.time_button.setText(_translate("MainWindow", "Время"))
player.tab.add_mag_lvl0_2.setText(_translate("MainWindow", "Добавить"))
player.tab.pushButton_4.setText(_translate("MainWindow", "Изменить"))
player.tab.pushButton_5.setText(_translate("MainWindow", "Удалить"))
player.tab.characters_tab.setTabText(player.tab.characters_tab.indexOf(player.tab), _translate("MainWindow", "Страница"))
player.tab.characters_tab.setTabText(player.tab.characters_tab.indexOf(player.tab), _translate("MainWindow", "Страница"))
player.tab.character_menu.setTitle(_translate("MainWindow", "Персонаж"))
player.tab.book_menu.setTitle(_translate("MainWindow", "Книга"))
player.tab.instruments_menu.setTitle(_translate("MainWindow", "Инструменты"))
player.tab.instr_character.setTitle(_translate("MainWindow", "Создание персонажа/npc"))
player.tab.name_generator.setTitle(_translate("MainWindow", "Генератор имен"))
player.tab.bandit_name_generator.setTitle(_translate("MainWindow", "Генератор имен бандитов"))
player.tab.harakter_generator.setTitle(_translate("MainWindow", "Генератор характера"))
player.tab.country_name_generator.setTitle(_translate("MainWindow", "Генератор названия станы"))
player.tab.make_location.setTitle(_translate("MainWindow", "Создание локаций"))
player.tab.home_generator.setTitle(_translate("MainWindow", "Генератор Таверн"))
player.tab.city_generator.setTitle(_translate("MainWindow", "Генератор карты города"))
player.tab.usefull_menu.setTitle(_translate("MainWindow", "Бестиарий/Предметы/Заклинания"))
player.tab.bestiary.setTitle(_translate("MainWindow", "Бестиарий"))
player.tab.items.setTitle(_translate("MainWindow", "Предметы"))
player.tab.magic_items.setTitle(_translate("MainWindow", "Маг. Предметы"))
player.tab.normal_items.setTitle(_translate("MainWindow", "Обычное оружие"))
player.tab.magic.setTitle(_translate("MainWindow", "Заклинания"))
player.tab.cubes.setTitle(_translate("MainWindow", "Кубики"))
player.tab.configs.setTitle(_translate("MainWindow", "Настройки"))
player.tab.vk_group.setTitle(_translate("MainWindow", "Вк группа"))
player.tab.help.setTitle(_translate("MainWindow", "Помощь"))
player.tab.add_character.setText(_translate("MainWindow", "Добавить"))
player.tab.add_character.setShortcut(_translate("MainWindow", "Ctrl+N"))
player.tab.load_character.setText(_translate("MainWindow", "Загрузить"))
player.tab.load_character.setShortcut(_translate("MainWindow", "Ctrl+L"))
player.tab.save_character.setText(_translate("MainWindow", "Сохранить всех"))
player.tab.save_character.setShortcut(_translate("MainWindow", "Ctrl+S"))
player.tab.master_book.setText(_translate("MainWindow", "Книга Мастера(offline)"))
player.tab.master_book.setShortcut(_translate("MainWindow", "Ctrl+M"))
player.tab.study_book.setText(_translate("MainWindow", "Книга Игрока(Offline)"))
player.tab.study_book.setShortcut(_translate("MainWindow", "Ctrl+P"))
player.tab.sounds.setText(_translate("MainWindow", "Звуковое сопровождение"))
player.tab.actionrpgtinker_com_country_name_generator.setText(_translate("MainWindow", "rpgtinker.com"))
player.tab.actionAutoNAME_AutoREALM_name_generator.setText(_translate("MainWindow", "AutoNAME(AutoREALM)"))
player.tab.actiontentaculus_ru_name_generator.setText(_translate("MainWindow", "tentaculus.ru"))
player.tab.actionstormtower_ru_bandit_name_generator.setText(_translate("MainWindow", "stormtower.ru"))
player.tab.actionrandomall_ru_harakter_generator.setText(_translate("MainWindow", "randomall.ru"))
player.tab.actionrandomall_ru_county_name_generator.setText(_translate("MainWindow", "randomall.ru"))
player.tab.actionstormtower_ru_home_generator.setText(_translate("MainWindow", "stormtower.ru(Описание)"))
player.tab.actionCampaign_Cartographer_3_CC3_city_generator.setText(
_translate("MainWindow", "Campaign Cartographer 3(CC3)"))
player.tab.actionAutoREALM_city_generator.setText(_translate("MainWindow", "AutoREALM"))
player.tab.actionpyromancers_com_city_generator.setText(_translate("MainWindow", "pyromancers.com"))
player.tab.actionwatabou_itch_io_city_generator.setText(_translate("MainWindow", "watabou.itch.io"))
player.tab.actiondungeon_su_bestiary.setText(_translate("MainWindow", "dungeon.su"))
player.tab.actiontentaculus_ru_bestiary.setText(_translate("MainWindow", "tentaculus.ru"))
player.tab.actiondungeon_su_magic_items.setText(_translate("MainWindow", "dungeon.su"))
player.tab.actiontentaculus_ru_magic_items.setText(_translate("MainWindow", "tentaculus.ru"))
player.tab.actiondungeon_su_normal_items.setText(_translate("MainWindow", "dungeon.su"))
player.tab.actiondnd5_club_normal_items.setText(_translate("MainWindow", "dnd5.club"))
player.tab.actiondungeon_su_magic.setText(_translate("MainWindow", "dungeon.su"))
player.tab.actiontentaculus_ru_magic.setText(_translate("MainWindow", "tentaculus.ru"))
player.tab.action1.setText(_translate("MainWindow", "1"))
player.tab.load_character.setObjectName("load_character")
player.tab.save_character = QtWidgets.QAction(MainWindow)
player.tab.save_character.setObjectName("save_character")
player.tab.master_book = QtWidgets.QAction(MainWindow)
player.tab.master_book.setObjectName("master_book")
player.tab.study_book = QtWidgets.QAction(MainWindow)
player.tab.study_book.setObjectName("study_book")
player.tab.sounds = QtWidgets.QAction(MainWindow)
player.tab.sounds.setObjectName("sounds")
player.tab.actionrpgtinker_com_country_name_generator = QtWidgets.QAction(MainWindow)
player.tab.actionrpgtinker_com_country_name_generator.setObjectName("actionrpgtinker_com_country_name_generator")
player.tab.actionAutoNAME_AutoREALM_name_generator = QtWidgets.QAction(MainWindow)
player.tab.actionAutoNAME_AutoREALM_name_generator.setObjectName("actionAutoNAME_AutoREALM_name_generator")
player.tab.actiontentaculus_ru_name_generator = QtWidgets.QAction(MainWindow)
player.tab.actiontentaculus_ru_name_generator.setObjectName("actiontentaculus_ru_name_generator")
player.tab.actionstormtower_ru_bandit_name_generator = QtWidgets.QAction(MainWindow)
player.tab.actionstormtower_ru_bandit_name_generator.setObjectName("actionstormtower_ru_bandit_name_generator")
player.tab.actionrandomall_ru_harakter_generator = QtWidgets.QAction(MainWindow)
player.tab.actionrandomall_ru_harakter_generator.setObjectName("actionrandomall_ru_harakter_generator")
player.tab.actionrandomall_ru_county_name_generator = QtWidgets.QAction(MainWindow)
player.tab.actionrandomall_ru_county_name_generator.setObjectName("actionrandomall_ru_county_name_generator")
player.tab.actionstormtower_ru_home_generator = QtWidgets.QAction(MainWindow)
player.tab.actionstormtower_ru_home_generator.setObjectName("actionstormtower_ru_home_generator")
player.tab.actionCampaign_Cartographer_3_CC3_city_generator = QtWidgets.QAction(MainWindow)
player.tab.actionCampaign_Cartographer_3_CC3_city_generator.setObjectName(
"actionCampaign_Cartographer_3_CC3_city_generator")
player.tab.actionAutoREALM_city_generator = QtWidgets.QAction(MainWindow)
player.tab.actionAutoREALM_city_generator.setObjectName("actionAutoREALM_city_generator")
player.tab.actionpyromancers_com_city_generator = QtWidgets.QAction(MainWindow)
player.tab.actionpyromancers_com_city_generator.setObjectName("actionpyromancers_com_city_generator")
player.tab.actionwatabou_itch_io_city_generator = QtWidgets.QAction(MainWindow)
player.tab.actionwatabou_itch_io_city_generator.setObjectName("actionwatabou_itch_io_city_generator")
player.tab.actiondungeon_su_bestiary = QtWidgets.QAction(MainWindow)