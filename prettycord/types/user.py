from prettycord.types import Deserializable


class User(Deserializable):
    __slots__ = ("data", "id", "first_name", "last_name", "username", "language_code")

    def __init__(
        self,
        data: dict,
        id: str,
        name: str,
        icon: str,
        owner: bool,
        permissions: str,
        features: list,
        approximate_member_count: int,
        approximate_presence_count: int,
    ):
        self.data = data
        self.id = id
        self.name = name
        self.icon = icon
        self.owner = owner
        self.permissions = permissions
        self.features = features
        self.approximate_member_count = approximate_member_count
        self.approximate_presence_count = approximate_presence_count

    @classmethod
    def de_json(cls, data: str or dict) -> "User":
        data = cls.check_json(data)

        id = data.get("id")
        name = data.get("name")
        icon = data.get("icon")
        owner = data.get("owner")
        permissions = data.get("permissions")
        features = data.get("features")
        approximate_member_count = data.get("approximate_member_count")
        approximate_presence_count = data.get("approximate_presence_count")

        return User(
            data,
            id,
            name,
            icon,
            owner,
            permissions,
            features,
            approximate_member_count,
            approximate_presence_count,
        )
