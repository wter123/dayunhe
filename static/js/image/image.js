var imgFullParams = {
  angle: 0,
  scale: 1,
  imgList: [],
  current: 0
}


var formGlobal = {
  taskBackstageAuditRemark: ""
}
function createURL(item) {
  return window.URL.createObjectURL(item);
}
function getFileFromUrl(url, fileName) {
  return new Promise((resolve, reject) => {
    var blob = null;
    var xhr = new XMLHttpRequest();
    xhr.open("GET", url);
    xhr.setRequestHeader('Accept', 'image/png');
    xhr.responseType = "blob";
    // 加载时处理
    xhr.onload = () => {
      // 获取返回结果
      blob = xhr.response;
      let file = new File([blob], fileName, { type: 'image/png' });
      // 返回结果
      resolve(file);
    };
    xhr.onerror = (e) => {
      reject(e)
    };
    // 发送
    xhr.send();
  });
}
function ulrToFile(url, name) {
  url=`http://127.0.0.1:5000/static${url}`
  let file = null
  return getFileFromUrl(url, name)
    .then((response) => {
      file = response
      imgFullParams.imgList.push(file)
    })
    .catch((e) => {
    });
}

function initFormGlobal(data) {
  let imageUpdate = $("#imageUpdate>.img_item")
  for (let i = 0; i < imageUpdate.length; i++) {
    imageUpdate[i].remove()
  }
  imgFullParams.imgList=[]
  formGlobal = data
  if (formGlobal.taskSubmitType) {
    $("input[name='submittype']").eq(formGlobal.taskSubmitType - 1).attr("checked", true)
    $("textarea[name='remark']").val(formGlobal.taskBackstageAuditRemark)
    $(`input[name='id']`).val(formGlobal.id)


    for (let i = 0; i < formGlobal.taskPhoto.length; i++) {
      $("#imageUpdate").append(`<div class="img_item" style="cursor:pointer;width: 100px;height: 100px;margin-left: 5px;flex:1;flex-shrink:0;">
    <img class="showimg" style="width: 100px;height: 100px;position: absolute; text-align: center;border:5px solid white;border-radius:10px" src="${formGlobal.taskPhoto[i].url}" />
  </div>`)
     ulrToFile(formGlobal.taskPhoto[i].url,formGlobal.taskPhoto[i].name)
    }


  }
}



function drag(obj) {
  obj.onmousedown = function (event) {

    //设置box1捕获所有鼠标按下的事件
    /*
     * setCapture()
     *  - 只有IE支持，但是在火狐中调用时不会报错
     * 		而如果使用chrome调用，会报错
     */
    obj.setCapture && obj.setCapture();


    event = event || window.event
    //div的偏移量，鼠标.clientX-元素.offsetLeft

    //div的偏移量，鼠标.clientY-元素.offsetTop

    var ol = event.clientX - obj.offsetLeft;

    var ot = event.clientY - obj.offsetTop;
    //为document绑定一个onmousemove事件

    document.onmousemove = function (event) {

      event = event || window.event
      //当鼠标移动时被拖拽的元素跟随鼠标移动 onmousemove

      //获取鼠标的坐标
      var left = event.clientX - ol;
      var top = event.clientY - ot;

      //修改box1的位置
      obj.style.left = left + "px";
      obj.style.top = top + "px";

    };


    //为元素绑定一个鼠标松开事件
    document.onmouseup = function () {
      //当鼠标松开时，被拖拽元素固定在当前位置 onmouseup
      //取消document的onmousemove事件

      document.onmousemove = null;
      document.onmouseup = null;
      //当鼠标松开时，取消对事件的捕获
      obj.releaseCapture && obj.releaseCapture();
    };
    /*
     * 当我们拖拽一个网页的内容时，浏览器会默认去搜索引擎中搜索内容
     *   此时会导致拖拽功能的异常，这是浏览器提供的默认行为
     * 	 如果不希望发生这个行为，则可以通过return false来取消默认行为
     */
    return false;
  };
};
var formDataGlobal = {}
$(function () {

  $("#submit").on("click", function (event) {
    let formdata = new FormData($("#form")[0]);
    // for (let i = 0; i < imgFullParams.imgList.length; i++) {
    //   formdata.append("goodsImg", imgFullParams.imgList[i])
    // }
    try {
      let goods_imgs = $("#myfile")

      for (var i = 0; i < imgFullParams.imgList.length; i++) {
        formdata.append("auditImgs", imgFullParams.imgList[i])
      }
    } catch (e) {
      console.log(e)
    }




    let entries = formdata.entries()
    formDataGlobal = Object.fromEntries(entries);
    console.log(formdata, formDataGlobal)

    $.ajax({
      url: '/audit/',
      type: 'POST',
      data: formdata,
      processData: false,
      contentType: false,
      success: function (data, textStatus, jqXHR) {
        location.reload();
      },
      error: function (jqXHR, textStatus, error) {
        // location.reload();
      }
    })
    event.preventDefault();

  })
  $("#delete__imgFull").on("click", function () {
    if (window.confirm("是否要删除此照片？")) {
      let imageUpdate = $("#imageUpdate>.img_item")
      imageUpdate[imgFullParams.current].remove()

      imgFullParams.imgList.splice(imgFullParams.current, 1)
      let current = imgFullParams.current - 1

      let length = $(".img_item").length
      if (length > 0) {
        imgFullParams.current = (imgFullParams.current + current + length) % length
        $("#img-entity").attr("src", createURL(imgFullParams.imgList[imgFullParams.current]))
      } else {
        $("#img-entity").attr("src", "")
        $('#img-full').hide()
      }
    } else {
    }
  })
  $(document).on({
    dragleave: function (e) {
      e.preventDefault();
    },
    drop: function (e) {
      e.preventDefault();
    },
    dragenter: function (e) {
      e.preventDefault();
    },
    dragover: function (e) {
      e.preventDefault();
    }
  });
  $("#imageUpdate").on("click", ".img_item", function () {
    imgFullParams.current = $(this).index() - 1

    $("#img-entity").attr("src", createURL(imgFullParams.imgList[imgFullParams.current]))
    $("#img-full").show()
  })



  var dropboxfile = document.getElementById("dropbox");
  dropboxfile.addEventListener('drop', function (e) {
    console.log(e)
    e.preventDefault();
    let fileList = e.dataTransfer.files;
    if (fileList.length == 0) {
      return false;
    }
    for (let i = 0; i < fileList.length; i++) {
      fileProp(fileList[i])
    }
    // var info = "<span>文件名'" + imgname + "'</span><span>文件大小'" + imgsize + "'kb</span>";
    // $("#inofimg").html(info);
  })


  document.onmousewheel = function (e) {
    if ($("#img-full").css("display") != "none") {
      if (e.wheelDelta > 0) {
        scale__imgFull(0.1)
        // console.log('向上滑');
      } else {
        scale__imgFull(-0.1)
        // console.log('向下滑');
      }
    }

  }





  /*
 * 拖拽box1的元素
 *  - 拖拽的流程
 *  	1.当鼠标在被拖拽的元素上按下时开始拖拽 onmousedown
 * 		2.当鼠标移动时被拖拽的元素跟随鼠标移动 onmousemove
 * 		3.当鼠标松开时被拖拽的对象固定到当前位置 onmouseup
 */
  var img01 = document.getElementById("img-entity")
  drag(img01);

  /*
   * 提取一个专门用来设置拖拽的函数
   * 参数，开启拖拽的元素
   */



})

var fileProp = function (file) {
  let imgname = file.name;
  if (file.type.indexOf('image') === -1) {
    alert(`${imgname} 该文件不是图片`);
    return false;
  }
  let imgurl = file;
  let imgsize = Math.floor((file.size) / 1024);
  if (imgsize > 1024) {
    alert(`${imgname} 文件大小不能超过1M`);
    return false;
  }


  $("#imageUpdate").append(`<div class="img_item" style="cursor:pointer;width: 100px;height: 100px;margin-left: 5px;flex:1;flex-shrink:0;">
          <img class="showimg" style="width: 100px;height: 100px;position: absolute; text-align: center;border:5px solid white;border-radius:10px" src="${window.URL.createObjectURL(imgurl)}" />
        </div>`)
  imgFullParams.imgList.push(imgurl)
}

function rotate__imgFull(rotate) {
  imgFullParams.angle = rotate + imgFullParams.angle
  let imgFull = $("#img-entity")
  imgFull.css("transform", `rotate(${imgFullParams.angle}deg)`)

}
function full__imgFull() {
  let imgEntity = $("#img-entity")
  if (imgEntity.css("transform") != "none") {
    imgEntity.removeClass("minWH").addClass("maxWH")
  } else {
    if (imgEntity.attr("class") == "maxWH") {
      imgEntity.removeClass("maxWH").addClass("minWH")
    } else {
      imgEntity.removeClass("minWH").addClass("maxWH")
    }
  }

  imgEntity.css("left", "inherit")
  imgEntity.css("top", "inherit")
  imgEntity.css("transform", "inherit")

  imgFullParams.angle = 0,
    imgFullParams.scale = 1
}
function scale__imgFull(scale) {
  if (imgFullParams.scale < 0.2) {
    imgFullParams.scale = 0.2
  }
  imgFullParams.scale = scale + imgFullParams.scale
  let imgFull = $("#img-entity")
  imgFull.css("transform", `scale(${imgFullParams.scale})`)
}

function next(current) {
  let length = $(".img_item").length
  console.log(length, current)
  imgFullParams.current = (imgFullParams.current + current + length) % length
  $("#img-entity").attr("src", createURL(imgFullParams.imgList[imgFullParams.current]))
}
function fileChange(e) {
  fileList = e.files
  for (let i = 0; i < fileList.length; i++) {
    fileProp(fileList[i])
  }
}
function fileDrop(e) {
  let fileList = e.dataTransfer.files;
  if (fileList.length == 0) {
    return false;
  }
  for (let i = 0; i < fileList.length; i++) {
    fileProp(fileList[i])
  }
}


