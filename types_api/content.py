from typing import TypedDict, Optional, List


class Channel(TypedDict):
    name: str
    id: str


class Author(TypedDict):
    username: str
    discriminator: str
    id: str
    avatarURL: str
    bot: bool


class Attachment(TypedDict):
    name: str
    fileurl: str
    width: Optional[str]
    height: Optional[str]
    content_type: str


class Guild(TypedDict):
    name: str
    id: str
    iconURL: str
        
        
class MessageReference(TypedDict):
    channel_id: Optional[str]
    guild_id: Optional[str]
    message_id: Optional[str]
        
        
class Message(TypedDict):
    content: str
    id: str
    cleanContent: str
    reference: MessageReference
    attachments: List[Attachment]
    embeds: list


class Content(TypedDict):
    channel: Channel
    author: Author
    guild: Guild
    message: Message
