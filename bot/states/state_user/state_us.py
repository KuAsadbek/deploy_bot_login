from aiogram.fsm.state import StatesGroup,State

class StateUser(StatesGroup):
    who = State()
    teacher_name = State()
    teacher_num = State()
    student_name = State()
    un_id = State()
    yep = State()
    ru = State()
    school = State()
    muc = State()
    name = State()
    city = State()
    number = State()
    py = State()
    py1 = State()
    check = State()
    comment = State()