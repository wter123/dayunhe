new Vue({
  el: '#app',
  data: function() {
    return {
         visible: false ,
         num:0,
        }
  },
  created(){
    this.fun()
  },
  methods:{
      fun(){
         if(this.num >=100)return
         setTimeout(()=>{
              this.num+=20
              this.fun()
          },1000)
      }
  }
})