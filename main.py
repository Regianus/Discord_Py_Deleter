import discord
import asyncio

async def delete_friends(client, override_usernames=[]):
    user_ids_to_keep = {
        overridden_user.id: overridden_user for overridden_user in await client.fetch_users(override_usernames).flatten()
    }

    friend_ids = [friend.id for friend in await client.fetch_user(client.user.id).friends()]
    for user_id in friend_ids:
        if user_id not in user_ids_to_keep:
            try:
                await client.user.remove_friend(user_ids_to_keep[user_id])
                print(f"Removed {user_ids_to_keep[user_id]}")
            except discord.HTTPException as e:
                print(f"Error removing {user_ids_to_keep[user_id]}: {e}")

TOKEN = "your_bot_token_here"
override_usernames = ["username1", "username2"]  # Ignore these users

intents = discord.Intents.default()
client = discord.Client(intents=intents)

asyncio.run(delete_friends(client, override_usernames))
