# Семестровый проект по курсу Совместная разработка приложений на Python»

## Участники:
* Подопросветов Андрей Валерьевич, группа 623, логин: Andrew
* Тимохин Иван Александрович, группа 623, логин: DeadSonger
* Николашкин Алексей Герасимович, группа 623, логин: nagvv

## Постановка задачи
Написать top-down шутер, в стиле Hotline Miami (хотя бы один уровень). 
Для работы с графикой предполагается использовать пакет [PyOpenGL](https://pypi.org/project/PyOpenGL/),
для работы с пользовательским оконным интерфейсом предполагается использовать [PyQt5](https://pypi.org/project/PyQt5/).


## Интерфейсная модель:

1) Главное меню:
   
   ![Главное меню](https://github.com/DeadSonger/cold_ray_norilsk/master/description/main_menu.png)
   
   На главном меню отражены три кнопки:
   * Новая игра, которая делает переход к игровому процессу
   * Настройки, которая делает переход к меню настроек
   * выход, которая завершает работу приложения

2) Меню настройки управления:
    
    ![Главное меню](https://github.com/DeadSonger/cold_ray_norilsk/master/description/settings_menu.png)
    
    Предосталяет доступ к настройкам управления, позволяя переназначать клавиши управления.

3) Игровой процесс:

    Главной целью игры является уничтожение противников на уровне, 
    подручными средствами, без получения урона. Персонаж входит на локацию безоружный.
