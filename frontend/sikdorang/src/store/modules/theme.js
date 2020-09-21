const theme = {
    namespaced : true,
    state : {
        themes : 
        [
            {"id":1, "theme_name":"빵집"},
            {"id":2, "theme_name":"케익"},
            {"id":3, "theme_name":"만두"},
            {"id":4, "theme_name":"떡볶이"},
            {"id":5, "theme_name":"짬뽕"},
            {"id":6, "theme_name":"짜장면"},
            {"id":7, "theme_name":"수제버거"},
            {"id":8, "theme_name":"돈가스"},
            {"id":9, "theme_name":"전국 터미널 맛집"},
            {"id":10, "theme_name":"기차역 맛집"},
            {"id":11, "theme_name":"고속도로 휴게소 맛집"},
            ]
    },
    getters : {
        getThemes : state => {
            return state.themes
        },
      
    },
    mutations : {
        mutationThemes: (state,payload) => {
            state.themes = payload
        },
       
    },
    actions : {
        actionThemes: ({commit}, payload) => {
            commit("mutationThemes", payload)
        },
        
    }
}

export default theme










