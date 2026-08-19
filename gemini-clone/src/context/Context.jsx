import{createContext,useState}from"react"
import{generateResponse}from"../config/gemini"

export const Context=createContext()

const ContextProvider=({children})=>{
const[sidebar,setSidebar]=useState(true)
const[input,setInput]=useState("")
const[loading,setLoading]=useState(false)
const[result,setResult]=useState("")
const[history,setHistory]=useState([])

const newChat=()=>{
setInput("")
setResult("")
}

const onSent=async(prompt)=>{
if(!prompt.trim())return

setLoading(true)
setInput("")

setHistory(prev=>{
const item=prompt.length>35?prompt.substring(0,35)+"...":prompt
return[...prev,item]
})

try{
const response=await generateResponse(prompt)
setResult(response)
}catch(error){
console.error("API ERROR:",error)
setResult("Gemini API Error: "+(error.message||"Unknown error"))
}

setLoading(false)
}

const contextValue={
sidebar,
setSidebar,
input,
setInput,
loading,
result,
history,
onSent,
newChat
}

return(
<Context.Provider value={contextValue}>
{children}
</Context.Provider>
)
}

export default ContextProvider