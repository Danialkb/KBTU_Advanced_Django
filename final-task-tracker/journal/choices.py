import enum


class RequestEnum(enum.Enum):
    ADD_USER = "ADD_USER"
    DELETE_USER = "DELETE_USER"

    ADD_TASK = "ADD_TASK"
    DELETE_TASK = "DELETE_TASK"

    ADD_TASK_COMMENT = "ADD_TASK_COMMENT"
    DELETE_TASK_COMMENT = "DELETE_TASK_COMMENT"

    ADD_CATEGORY = "ADD_CATEGORY"
    DELETE_CATEGORY = "DELETE_CATEGORY"
    CODE_REVIEW_DONE = "CODE_REVIEW_DONE"
    STAGE = "STAGE"
