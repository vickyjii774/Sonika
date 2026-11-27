const BASE=(import.meta.env.VITE_API_URL||"http://127.0.0.1:8000/api").replace(/\/$/,"");
export async function api(path,{token,...opts}={}){
  const res=await fetch(BASE+path,{...opts,headers:{"Content-Type":"application/json",...(token?{Authorization:`Bearer ${token}`}:{}),...(opts.headers||{})}});
  const raw=await res.text();
  let data={};
  try{data=raw?JSON.parse(raw):{};}catch{data={detail:raw||"The server returned an unreadable response."};}
  if(!res.ok){
    const message=data.detail||data.error||data.message||"Request failed";
    throw new Error(`${message} (HTTP ${res.status})`);
  }
  return data;
}
export{BASE};