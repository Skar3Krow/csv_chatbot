css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #222429
}
.chat-message.bot {
    background-color: #1a1b1f
}

.chat-message .avatar  {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 0rem;
  color: #fff;
}
.st-emotion-cache-1y4p8pa{
padding:2rem 1rem 10rem;
}
.fleex{
display:flex;
flex-direction:column;
width:100%;
}
.you{
font-weight:900;
}

'''

bot_template = '''
<div class="chat-message bot">
    <div class="fleex">
    <div class="you">CSV-GPT</div>
    <div class="message">{{MSG}}</div>
    </div>
    
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
    </div>
    <div class="fleex">
    <div class="you">User</div>
    <div class="message">{{MSG}}</div>
    </div>
</div>
'''
