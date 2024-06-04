from fastapi import Depends, HTTPException, status
from fastapi.routing import APIRouter

from application.api.messages.schemas import CreateChatRequestSchema, CreateChatResponseSchema
from application.api.schemas import ErrorSchema
from domain.exceptions.base import ApplicationException
from logic.commands.messages import CreateChatCommand
from logic.exceptions.base import LogicException
from logic.init import init_container
from logic.mediator import Mediator


router = APIRouter(
    prefix='',
    tags=['Chat'],
)


@router.post(
    '/',
    response_model=CreateChatResponseSchema,
    status_code=status.HTTP_201_CREATED,
    description="Endpoint for new chat creation",
    responses={
        status.HTTP_201_CREATED: {'model': CreateChatResponseSchema},
        status.HTTP_400_BAD_REQUEST: {'model': ErrorSchema},
    }
)
async def create_chat_handler(schema: CreateChatRequestSchema, container=Depends(init_container)):
    """Creation of new chat"""
    mediator: Mediator = container.resolve(Mediator)

    try:
        chat, *_ = await mediator.handle_command(CreateChatCommand(title=schema.title))
    except LogicException as exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={'error': exception.message})
    
    return CreateChatResponseSchema.from_entity(chat)