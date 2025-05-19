from .commands import router as commands_router
from .texts import router as texts_router
from .callbacks import router as callbacks_router
from .food_callbacks import router as food_callbacks_router
from .add_to_callbacks import router as add_to_callbacks_router
from .product_callbacks import router as product_callbacks_router

routers_list = [
    commands_router,
    texts_router,
    callbacks_router,
    food_callbacks_router,
    add_to_callbacks_router,
    product_callbacks_router,
]