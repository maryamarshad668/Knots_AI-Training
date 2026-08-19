import{useContext}from"react"
import{Context}from"../../context/Context"
import"./Sidebar.css"

const Sidebar=()=>{
const{sidebar,setSidebar,history,newChat}=useContext(Context)

return(
<div className={`sidebar ${sidebar?"":"closed"}`}>
<div className="top">
<button className="menu" onClick={()=>setSidebar(!sidebar)}>☰</button>
{sidebar&&(
<>
<button className="new-chat" onClick={newChat}>＋</button>
<span>New Chat</span>
</>
)}
</div>

{sidebar&&(
<div className="history">
<h3>Recent</h3>
{history.length===0?(
<p className="empty">No chats yet</p>
):(
history.map((item,index)=>(
<div className="history-item" key={index}>
<span>💬</span>
<p>{item}</p>
</div>
))
)}
</div>
)}

<div className="bottom">
<div>⚙️ {sidebar&&<span>Settings</span>}</div>
<div>❓ {sidebar&&<span>Help</span>}</div>
</div>
</div>
)
}

export default Sidebar