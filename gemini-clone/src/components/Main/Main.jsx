import{useContext,useEffect,useRef,useState}from"react"
import{Context}from"../../context/Context"
import"./Main.css"

const Main=()=>{
const{input,setInput,result,loading,onSent}=useContext(Context)
const[lastPrompt,setLastPrompt]=useState("")
const resultRef=useRef()

const cards=[
"Explain artificial intelligence in simple words",
"Give me 5 ideas for a Python project",
"How does machine learning work?",
"Create a study plan for learning React"
]

useEffect(()=>{
if(result&&resultRef.current){
resultRef.current.innerHTML=result
.replace(/\*\*(.*?)\*\*/g,"<strong>$1</strong>")
.replace(/\n/g,"<br/>")
}
},[result])

const submit=prompt=>{
const value=prompt||input

if(!value.trim())return

setLastPrompt(value)
onSent(value)
}

const handleKeyDown=e=>{
if(e.key==="Enter"&&!e.shiftKey){
e.preventDefault()
submit()
}
}

return(
<div className="main">
<div className="nav">
<span>Gemini Clone</span>
<div className="profile">M</div>
</div>

{!result&&!loading?(
<div className="welcome">
<h1>Hello, Maryam</h1>
<h2>How can I help you today?</h2>

<div className="cards">
{cards.map((card,index)=>(
<div className="card" key={index} onClick={()=>submit(card)}>
<p>{card}</p>
<span>→</span>
</div>
))}
</div>
</div>
):(
<div className="chat">
<div className="user-message">
<div className="user-icon">M</div>
<p>{lastPrompt}</p>
</div>

<div className="ai-message">
<div className="ai-icon">✦</div>

{loading?(
<div className="loader">
<span></span>
<span></span>
<span></span>
</div>
):(
<div ref={resultRef} className="response"></div>
)}
</div>
</div>
)}

<div className="input-area">
<div className="input-box">
<textarea
value={input}
onChange={e=>setInput(e.target.value)}
onKeyDown={handleKeyDown}
placeholder="Enter a prompt here"
rows="1"
/>

<div className="input-bottom">
<span>＋</span>
<button onClick={()=>submit()}>➤</button>
</div>
</div>

<p>Gemini Clone can make mistakes. Check important information.</p>
</div>
</div>
)
}

export default Main