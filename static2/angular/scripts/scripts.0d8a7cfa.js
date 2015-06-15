"use strict";
angular.module("app", ["app.core", "app.blocks", "app.services", "app.wizard", "app.home"]), angular.module("app.core", [ "ui.router", "ngSanitize", "ngStorage", "ngCookies", "angular-loading-bar"]), angular.module("app.services", []).constant("baseUrl", "http://localhost:8000/dashboard/api/").constant("token", "Token c4e913f4877e6762b8458b4d349ed402a5c3a842")//61e7de5eae825fe98dbb8e1ad714a97d4fc090f8")
    .factory("Types", ["$http", "$q", "baseUrl", function (a, b, c) {
    return{getAll: function () {
        a.defaults.withCredentials = !1;
        var d = b.defer(), e = d.promise, f = "types/";
        return a.get(c + f).success(function (a) {
            d.resolve(a)
        }).error(function (a) {
            d.reject(a)
        }), e
    }, getById: function (d) {
        var e = b.defer(), f = e.promise, g = "types/";
        return a.get(c + g + d).success(function (a) {
            e.resolve(a)
        }).error(function (a) {
            e.reject(a)
        }), f
    }}
}]).factory("Products", ["$http", "$q", "baseUrl", function (a, b, c) {
    return{getAll: function (d) {
        a.defaults.withCredentials = !1;
        var e = b.defer(), f = e.promise, g = "/products/";
        return a.get(c + "types/" + d + g).success(function (a) {
            e.resolve(a)
        }).error(function (a) {
            e.reject(a)
        }), f
    }, getById: function (d) {
        var e = b.defer(), f = e.promise, g = "products/";
        return a.get(c + g + d).success(function (a) {
            e.resolve(a)
        }).error(function (a) {
            e.reject(a)
        }), f
    }}
}]).factory("Price", ["$http", "$q", "baseUrl", function (a, b, c) {
    return{get: function (d) {
        a.defaults.withCredentials = !1;
        var e = b.defer(), f = e.promise, g = "products/";
        return a.get(c + g + d + "/stockrecords").success(function (a) {
            e.resolve(a)
        }).error(function (a) {
            e.reject(a)
        }), f
    }}
}]).factory("Event", ["$http", "$q", "baseUrl", function (a, b, c) {
    return{get: function () {
        a.defaults.withCredentials = !1;
        var d = b.defer(), e = d.promise, f = "events/";
        return a.get(c + f).success(function (a) {
            d.resolve(a)
        }).error(function (a) {
            d.reject(a)
        }), e
    }}
}]).factory("Template", ["$http", "$q", "baseUrl", function (a, b, c) {
    return{get: function (d) {
        a.defaults.withCredentials = !1;
        var e = b.defer(), f = e.promise, g = "/templates/";
        return a.get(c + "events/" + d + g).success(function (a) {
            e.resolve(a)
        }).error(function (a) {
            e.reject(a)
        }), f
    }}
}]).factory("UploadImage", ["$http", "$q", "baseUrl", "token", function (a, b, c, d) {
    return{file: function (e) {
        a.defaults.withCredentials = !1;
        var f = b.defer(), g = f.promise, h = "uploadimages/";
        return a.post(c + h, e, {headers: {"Content-Type": void 0, Authorization: d}, transformRequest: angular.identify}).success(function (a) {
            f.resolve(a)
        }).error(function (a) {
            f.reject(a)
        }), g
    }}
}]).factory("UploadLabel", ["$http", "$q", "baseUrl", "token", function (a, b, c, d) {
    return{send: function (e) {
        a.defaults.withCredentials = !1;
        var f = b.defer(), g = f.promise, h = "labels/";
        return a.post(c + h, e, {headers: {"Content-Type": "application/json", Authorization: d}}).success(function (a) {
            f.resolve(a)
        }).error(function (a) {
            f.reject(a)
        }), g
    }}
}]).factory("Matriz", [function () {
    return{transform: {}}
}]).factory("Oscar", ["$http", "$q", function (a, b) {
    return a.defaults.withCredentials = !0, {send: function (c, d) {
        console.log("sevice says " + typeof d);
        var e = b.defer(), f = e.promise;
        return a.post(c, d, {headers: {"Content-Type": "application/x-www-form-urlencoded"}, transformRequest: angular.identify}).success(function (a) {
            e.resolve(a)
        }).error(function (a) {
            e.reject(a)
        }), console.log(a.defaults), f
    }}
}]), angular.module("app.blocks", []).directive("hsBackSlider", ["$timeout", function (a) {
    return{scope: {source: "=", options: "="}, restrict: "AE", link: function (b, c, d) {
        var e = null, f = {mode: "timer", effect: "slidefade", effectTime: 1500, timerDelay: 1e4, centerImages: !0};
        _.isEmpty(b.options) || angular.extend(f, b.options), b.$watch("source", function (b) {
            _.isEmpty(b) && (_.isUndefined(b) || _.isNull(b)) || a(function () {
                e = c.backslider(f)
            }, 0)
        })
    }}
}]).directive("thTequilaCard", [function () {
    return{restrict: "A", scope: {type: "=tqType", size: "@tqSize", selected: "&tqSelected"}, transclude: !0, template: ['<div class="tq-card">', '<div class="tq-card__panel" ng-click="onSelectType(type);">', '<div class="tq-card__body">', '<img ng-src="{{ type.bimage }}" height="{{ size }}" />', '<h2 class="tq-card__name"> {{ type.name }}</h2>', "</div>", "</div>", "</div>"].join(""), link: function (a) {
        a.onSelectType = function (b) {
            a.selected(b)
        }
    }}
}]).directive("thWizardStep", ["$compile", function (a) {
    return{restrict: "E", scope: {ref: "@stepRef", valid: "=stepValid", step: "=step"}, template: ['<a class="step">', '<span class="step__dot">{{ step.id }}</span>', '<span class="step__label">{{ step.label }}</span>', "</a>"].join(""), transclude: !0, replace: !0, link: function (b, c, d) {
        a(c)(b), b.$watch("valid", function (d) {
            d ? (c.attr("ui-sref", b.ref), c.attr("ui-sref-active", "active")) : (c.removeAttr("ui-sref"), c.removeAttr("href")), a(c)(b)
        })
    }}
}]).directive("thCarousel", ["$timeout", function (a) {
    var b = null;
    return{restrict: "A", scope: {source: "=thSource"}, link: function (c, d) {
        var e = !1;
        b = d.children(".jcarousel"), c.$watch("source", function (c) {
            e ? b.jcarousel("reload") : _.isEmpty(c) || (a(function () {
                b.jcarousel({})
            }, 0), e = !0)
        })
    }, controller: ["$scope", "$attrs", function (a, c) {
        c.thCarousel && (a.$parent[c.thCarousel] = this), this.next = function () {
            b.jcarousel("scroll", "+=1")
        }, this.prev = function () {
            b.jcarousel("scroll", "-=1")
        }
    }]}
}]).directive("thFileInput", ["$parse", function (a) {
    return{restrict: "A", link: function (b, c, d) {
        c.bind("change", function () {
            a(d.thFileInput).assign(b, c[0].files), b.$apply()
        })
    }}
}]).directive("thTransformImage", ["$window", "$document", "Matriz", function (a, b, c) {
    return{scope: {image: "=thImage"}, restrict: "E", templateUrl: "static/angular/views/thtransform.tpl.html", replace: !0, transclude: !0, link: function (d, e) {
        d.matriz = c;
        var f = !1, g = "ontouchstart"in a || a.navigator.msPointerEnable ? !0 : !1, h = g ? {start: "touchstart", end: "touchend", move: "touchmove"} : {start: "mousedown", end: "mouseup", move: "mousemove"}, i = 1, j = function (a) {
            var b = 0, c = 0;
            return a.originalEvent.targetTouches ? (b = a.originalEvent.targetTouches[0].pageX, c = a.originalEvent.targetTouches[0].pageY) : a.pageX || a.pageY ? (b = a.pageX, c = a.pageY) : (a.clientX || a.clientY) && (b = a.clientX + document.body.scrollLeft + document.documentElement.scrollLeft, c = a.clientY + document.body.scrollTop + document.documentElement.scrollTop), {x: b, y: c}
        }, k = function (a, b, c) {
            return Math.min(Math.max(a, b), c)
        }, l = {init: function () {
            return this.cache(), this
        }, reload: function () {
            var a = this;
            a.unbind(), a.cache()
        }, cache: function () {
            var a = this;
            a.dragArea = e.find(".tfm-area"), a.dragImage = e.find(".tfm-image"), a.dragMask = e.find(".tfm-mask"), a.dragImage.css({width: "auto", top: 0, left: 0}), a.initVectors(), a.centerImage(), this.bind()
        }, centerImage: function () {
            var a = this;
            a.dragImage.one("load", function () {
                var b = a.rect($(this)), c = a.rect(a.dragMask), e = b.width / b.height, f = e > 1 ? "horizontal" : "vertical", g = 0, h = 0;
                "vertical" === f ? (g = 1.2 * c.width, h = g / e, $(this).width(g), $(this).height(h)) : "horizontal" === f && (h = 1.2 * c.height, g = h * e, $(this).width(g), $(this).height(h));
                var j = .5 * (c.width - $(this).width()), k = .5 * (c.height - $(this).height());
                l.vector.imgInit.x = j, l.vector.imgInit.y = k, l.imgRect = {width: g, height: h, top: k, left: j}, d.$apply(function () {
                    d.matriz.transform.left = l.imgRect.left * i, d.matriz.transform.top = l.imgRect.top * i, d.matriz.transform.width = l.imgRect.width * i, d.matriz.transform.height = l.imgRect.height * i
                }), $(this).css({left: j, top: k})
            }).each(function () {
                this.complete && $(this).load()
            })
        }, initVectors: function () {
            var a = this;
            a.vector = {init: {x: 0, y: 0}, current: {x: 0, y: 0}, imgInit: {x: 0, y: 0}, imgDest: {x: 0, y: 0}}
        }, scale: function (a) {
            var b = this, c = k(a.value * b.imgRect.width, b.imgRect.width, b.imgRect.width * a.max), e = c * b.imgRect.height / b.imgRect.width, f = b.vector.imgInit.y, g = b.vector.imgInit.x, h = a.value / a.lastValue, j = h * f + (1 - h) * b.dragMask.outerHeight(!0) / 2, l = h * g + (1 - h) * b.dragMask.outerWidth(!0) / 2;
            j = k(j, b.dragMask.outerHeight(!0) - e, 0), l = k(l, b.dragMask.outerWidth(!0) - c, 0), b.dragImage.css({width: c, height: e, top: j, left: l}), d.$apply(function () {
                d.matriz.transform.left = l * i, d.matriz.transform.top = j * i, d.matriz.transform.width = c * i, d.matriz.transform.height = e * i
            })
        }, lastPosition: function () {
            var a = this, b = a.dragImage.position();
            a.vector.imgInit.x = b.left, a.vector.imgInit.y = b.top
        }, bind: function () {
            var a = this;
            a.dragArea.on(h.start, a.onStartHandler)
        }, onStartHandler: function (a) {
            this.allowUp = this.scrollTop > 0, this.allowDown = this.scrollTop < this.scrollHeight - this.clientHeight, this.prevTop = null, this.prevBot = null, this.lastY = a.pageY, l.vector.init.x = j(a).x, l.vector.init.y = j(a).y, b.on(h.end, l.onEndHandler), b.on(h.move, l.onMoveHandler), l.dragImage.on("dragstart", function (a) {
                a.preventDefault()
            })
        }, onEndHandler: function (a) {
            b.off(h.move, l.onMoveHandler), b.off(h.end, l.onEndHandler)
        }, onMoveHandler: function (a) {
            var b = a.pageY > this.lastY, c = !b;
            this.lastY = a.pageY, b && this.allowUp || c && this.allowDown ? a.stopPropagation() : a.preventDefault();
            var e = j(a), f = {top: l.dragMask.outerHeight() - l.dragImage.height(), left: l.dragMask.outerWidth() - l.dragImage.width(), right: 0, bottom: 0};
            l.vector.current.x = e.x, l.vector.current.y = e.y;
            var g = l.vector.current.x - l.vector.init.x, h = l.vector.current.y - l.vector.init.y, m = k(l.vector.imgInit.x + g, f.left, f.right), n = k(l.vector.imgInit.y + h, f.top, f.bottom);
            l.vector.imgDest.x = m, l.vector.imgDest.y = n, l.dragImage.css({left: l.vector.imgDest.x, top: l.vector.imgDest.y}), l.vector.init.x = l.vector.current.x, l.vector.init.y = l.vector.current.y, l.vector.imgInit.x = l.vector.imgDest.x, l.vector.imgInit.y = l.vector.imgDest.y, d.$apply(function () {
                d.matriz.transform.left = l.vector.imgDest.x * i, d.matriz.transform.top = l.vector.imgDest.y * i
            })
        }, unbind: function () {
        }, rect: function (a) {
            return a[0].getBoundingClientRect()
        }}, m = {init: function () {
            var a = this;
            return a.data = {min: 1, max: 3, value: 1, lastValue: 1}, this.cache(), this
        }, reload: function () {
            var a = this;
            a.unbind(), a.cache()
        }, cache: function () {
            var a = this;
            a.thumb = e.find(".tfm-range-thumb"), a.track = e.find(".tfm-range-track"), a.thumb.css({top: 0, left: 0}), a.data.value = 1, a.data.lastValue = 1, a.bound = {min: a.track.position().left, max: a.track.width() - a.thumb.width()}, a.offsetX = 0, a.bind()
        }, bind: function () {
            var a = this;
            a.thumb.on(h.start, a.onStartHandler)
        }, onStartHandler: function (a) {
            a.preventDefault(), m.offsetX = j(a).x - m.thumb.position().left, b.on(h.end, m.onEndHandler), b.on(h.move, m.onMoveHandler)
        }, onEndHandler: function (a) {
            b.off(h.end, m.onEndHandler), b.off(h.move, m.onMoveHandler), m.data.lastValue = m.data.value, l.lastPosition()
        }, onMoveHandler: function (a) {
            var b = j(a), c = (m.data.max - m.data.min) / (m.bound.max - m.bound.min), d = b.x - m.offsetX, e = k(d, m.bound.min, m.bound.max), f = (d - m.bound.min) * c + m.data.min;
            m.thumb.css({left: e}), f = k(f, m.data.min, m.data.max), m.data.value = f, l.scale(m.data)
        }, unbind: function () {
            m.thumb.off(h.start, m.onStartHandler)
        }};
        d.$watch("image", function (a) {
            f ? (l.reload(), m.reload()) : _.isUndefined(a) || _.isEmpty(a) || (l.init(), m.init(), f = !0)
        }), d.isVisible = !0, d.toggleTransform = function () {
            d.isVisible = !d.isVisible
        }
    }}
}]).directive("thLabelImage", ["Matriz", function (a) {
    return{scope: {image: "=thImage", label: "=thLabel", build: "=thBuild"}, templateUrl: "static/angular/views/thlabel.tpl.html", replace: !0, link: function (b, c) {
        b.matriz = a;
        var d = !1, e = c.parent();
        b.$watch("image", function (a) {
            d || _.isUndefined(a) || _.isEmpty(a) || (d = !0)
        }), b.$watch("build", function (a) {
            a && html2canvas(e, {onrendered: function (a) {
                b.$apply(function () {
                    b.label = a.toDataURL()
                })
            }})
        })
    }}
}]), angular.module("app.home", []).config(["$stateProvider", "$urlRouterProvider", function (a, b) {
    a.state("home", {url: "/", templateUrl: "static/angular/views/home.html", controller: "HomeCtrl"}), b.otherwise("/")
}]).controller("HomeCtrl", ["$scope", "$sessionStorage", "$state", function (a, b, c) {
    a.$storage = b, a.$storage.steps = {}, console.log(a.$storage), a.slides = [
        {heading: "Tu Momento Especial", text: "Porque siempre hay esa canción, aroma, lugar que lo revive.", image: "static/angular/images/slides/1.jpg", action: "Comience ahora", position: "top-left"},
        {heading: "A un Recuerdo Eterno", text: "Conservar es asegurar que no se olvide.", image: "static/angular/images/slides/3.jpg", action: "Envíe su pedido hoy", position: "top-right"}
    ], a.startCustomizing = function () {
        c.go("wizard.type")
    }
}]), angular.module("app.wizard", ["app.wizard.type", "app.wizard.order", "app.wizard.event", "app.wizard.design", "app.wizard.summary"]).config(["$stateProvider", "$urlRouterProvider", function (a, b) {
    a.state("wizard", {url: "/wizard", "abstract": !0, templateUrl: "static/angular/views/wizard/wizard.html", controller: "WizardCtrl"}), b.otherwise("/wizard/type")
}]).controller("WizardCtrl", ["$scope", "$rootScope", "$state", "$sessionStorage", function (a, b, c, d) {
    a.$storage = d;
    var e = [
        {id: 1, ref: "type", label: "Tequila", valid: !0},
        {id: 2, ref: "order", label: "Pedido", valid: !1},
        {id: 3, ref: "event", label: "Evento", valid: !1},
        {id: 4, ref: "design", label: "Diseño", valid: !1},
        {id: 5, ref: "summary", label: "Resumen", valid: !1}
    ], f = "wizard.";
    _.isEmpty(a.$storage.steps) && (a.$storage.steps = e), a.$on("stepChange", function (b, d) {
        d.isValid && (a.$storage.steps[d.index + 1].valid = !0, c.go(f + a.$storage.steps[d.index + 1].ref))
    })
}]), angular.module("app.wizard.type", []).config(["$stateProvider", "$urlRouterProvider", function (a, b) {
    a.state("wizard.type", {url: "/type", templateUrl: "static/angular/views/wizard/type.html", controller: "TypeCtrl"}), b.otherwise("/")
}]).controller("TypeCtrl", ["$scope", "$sessionStorage", "Types", function (a, b, c) {
    a.types = [], a.typeSelected = {}, a.typeId = null, a.$storage = b, a.isValid = !1, a.$storage.data = {}, delete a.$storage.order;
    for (var d = 0; d < a.$storage.steps.length; d++)d > 0 && (a.$storage.steps[d].valid = !1);
    c.getAll().then(function (b) {
        a.types = b
    })["catch"](function (a) {
        console.log("error" + a)
    }), a.selected = function (b) {
        return a.typeSelected = b, a.typeId = b.id, _.isNull(a.typeId) || _.isUndefined(a.typeId) || !_.isString(a.typeId) ? (a.$storage.data.typeId = a.typeId, _.isNull(a.$storage.data.typeId) || _.isUndefined(a.$storage.data.typeId) ? a.isValid = !1 : a.isValid = !0, void a.$emit("stepChange", {index: 0, isValid: a.isValid})) : void parseInt(a.typeId, 10)
    }
}]), angular.module("app.wizard.order", []).config(["$stateProvider", "$urlRouterProvider", function (a, b) {
    a.state("wizard.order", {url: "/order", templateUrl: "static/angular/views/wizard/order.html", controller: "OrderCtrl"}), b.otherwise("/")
}]).controller("OrderCtrl", ["$scope", "$sessionStorage", "Products", "Price", function (a, b, c, d) {
    var e = 1;
    a.$storage = b, a.products = [], a.product = {}, a.qty = _.has(a.$storage.order, "qty") ? a.$storage.order.qty : e, a.isValid = !1;
    for (var f = 0; f < a.$storage.steps.length; f++)f > 1 && (a.$storage.steps[f].valid = !1);
    c.getAll(a.$storage.data.typeId).then(function (b) {
        if (a.products = b, !_.isNull(a.$storage.order) && !_.isUndefined(a.$storage.order)) {
            var c = _.findIndex(a.products, function (b) {
                return b.id === a.$storage.order.productId
            });
            a.product = a.products[c]
        }
    })["catch"](function (a) {
        console.log("error" + a)
    }), a.$watch("product", function (b) {
        _.isEmpty(b) || (a.isValid = !0, d.get(b.id).then(function (b) {
            a.productPrice = b[0], a.priceTotal = a.qty * a.productPrice.price_excl_tax
        })["catch"](function (a) {
            console.log(a)
        }))
    }), a.$watch("qty", function (b) {
        _.isUndefined(b) || _.isUndefined(a.productPrice) || (a.qty = a.qty >= 1 ? b : e, a.priceTotal = a.qty * a.productPrice.price_excl_tax)
    }), a.saveOrder = function () {
        (_.isNull(a.$storage.order) || _.isUndefined(a.$storage.order)) && (a.$storage.order = {}, a.isValid = !1), _.isNull(a.product.id) || _.isUndefined(a.product.id) ? a.isValid = !1 : (a.$storage.order.productId = a.product.id, a.$storage.order.qty = a.qty, a.$storage.order.priceTotal = a.pricetTotal, a.$storage.order.cycle = {index: 1, length: a.qty * a.product.maxlabels}, a.$storage.order.labels = [], a.$storage.order.price = {value: a.productPrice.price_excl_tax, currency: a.productPrice.price_currency}, a.isValid = !0), a.$emit("stepChange", {index: 1, isValid: a.isValid})
    }
}]), angular.module("app.wizard.event", []).config(["$stateProvider", "$urlRouterProvider", function (a, b) {
    a.state("wizard.event", {url: "/event", templateUrl: "static/angular/views/wizard/event.html", controller: "EventCtrl"}), b.otherwise("/")
}]).controller("EventCtrl", ["$scope", "$sessionStorage", "Event", "Template", function (a, b, c, d) {
    a.$storage = b, a.events = [], a.templates = [], a.isValid = !0, a.carousel;
    for (var e = 0; e < a.$storage.steps.length; e++)e > 2 && (a.$storage.steps[e].valid = !1);
    c.get().then(function (b) {
        a.events = b
    })["catch"](function (a) {
        console.log(a)
    }), a.getTemplates = function (b) {
        console.log("id : " + b), d.get(b).then(function (b) {
            a.templates = b
        })["catch"](function (a) {
            console.log(a)
        })
    };
    var f = a.$storage.order.labels.length, g = a.$storage.order.cycle.index;
    g === f && a.$storage.order.labels.pop(), a.chooseTemplate = function (b) {
        var c = {template: b, headlines: []};
        a.$storage.order.labels.push(c), a.$emit("stepChange", {index: 2, isValid: a.isValid})
    }
}]), angular.module("app.wizard.design", []).config(["$stateProvider", "$urlRouterProvider", function (a, b) {
    a.state("wizard.design", {url: "/design", templateUrl: "static/angular/views/wizard/design.html", controller: "DesignCtrl"}), b.otherwise("/")
}]).controller("DesignCtrl", ["$scope", "$sessionStorage", "$state", "Products", "UploadImage", "UploadLabel", "Matriz", function (a, b, c, d, e, f, g) {
    a.$storage = b, a.matriz = g, a.isValid = !1, a.cycleIndex = a.$storage.order.cycle.index, console.log(a.$storage.order.labels), a.template = a.$storage.order.labels[a.cycleIndex - 1].template, a.labelRender = void 0, a.labelBuild = !1, a.toRender = function () {
        a.labelBuild = !0
    }, a.fontStacks = [
        {name: "Arial", stack: "sans-a"},
        {name: "Times New Roman", stack: "serif-a"},
        {name: "Comic Sans MS", stack: "sans-b"},
        {name: "Georgia", stack: "serif-b"}
    ], a.matriz.firstTl = "Texto Primario", a.matriz.secondTl = "Texto Secundario", a.matriz.font = a.fontStacks[0];
    for (var h = 0; h < a.$storage.steps.length; h++)h > 3 && (a.$storage.steps[h].valid = !1);
    _.has(a.$storage.order.labels[a.cycleIndex - 1], "processedLabel") && (delete a.$storage.order.labels[a.cycleIndex - 1].processedLabel, console.log("etiqueta eliminada..sorry x(")), a.$watch("labelRender", function (b) {
        if (!_.isUndefined(b) && !_.isNull(b)) {
            var c = {uploadimage: a.labelImage.id, label: a.labelRender, name: ""};
            console.log(c), f.send(c).then(function (b) {
                _.isEmpty(b) || _.isNull(b) || _.isUndefined(b) ? a.isValid = !1 : (a.processedLabel = b, a.$storage.order.labels[a.cycleIndex - 1].processedLabel = a.processedLabel, a.isValid = !0), a.$emit("stepChange", {index: 3, isValid: a.isValid})
            })["catch"](function (a) {
                console.log(a)
            })
        }
    }), d.getById(a.$storage.order.productId).then(function (b) {
        a.product = b
    })["catch"](function (a) {
        console.log(a)
    }), a.uploadImage = function () {
        var b = new FormData;
        angular.forEach(a.files, function (a) {
            b.append("file", a)
        }), _.isUndefined(a.files) || _.isNull(a.files) ? (alert("error upload image required"), a.isValid = !1) : e.file(b).then(function (b) {
            a.uploadImage = b, a.labelImage = b
        })["catch"](function (a) {
            console.log(a)
        })
    }
}]), angular.module("app.wizard.summary", []).config(["$stateProvider", "$urlRouterProvider", function (a, b) {
    a.state("wizard.summary", {url: "/summary", templateUrl: "static/angular/views/wizard/summary.html", controller: "SummaryCtrl"}), b.otherwise("/")
}]).controller("SummaryCtrl", ["$scope", "$sessionStorage", "$state", "$cookies", "$window", "Oscar", "baseUrl", function (a, b, c, d, e, f, g) {
    a.$storage = b, a.maxLabels = a.$storage.order.cycle.length, a.currentLabels = a.$storage.order.cycle.index - 1, a.labels = a.$storage.order.labels, a.isAllowed = !0, a.index = a.$storage.order.cycle.index, a.continueDesigning = function () {
        var b = a.$storage.order.cycle.index, d = a.$storage.order.cycle.length;
        d > b ? (a.$storage.order.cycle.index++, a.isAllowed = !0) : (a.$storage.order.cycle.index = a.$storage.order.cycle.length, a.isAllowed = !1), a.isAllowed ? c.go("wizard.event") : alert("Has completado el número de etiquetas disponibles.")
    };
    var h = [];
    _.forEach(a.labels, function (a) {
        var b = {template: a.template.id, label: a.processedLabel.id};
        h.push(b)
    });
    var i = g.replace("dashboard/api/", "basket/add/") + a.$storage.order.productId + "/",
        labels = [], n=0;

    for (n=0; n< a.$storage.order.labels.length ; n++){
        labels.push(a.$storage.order.labels[n].processedLabel.id);
    }

    console.log(i), a.cart = {csrfmiddlewaretoken: d.get("csrftoken"), quantity: a.$storage.order.qty, labels: labels},
        a.checkout = function () {
        d.put('test', 'value');
        console.log(d.getAll());

        f.send(i, $.param(a.cart)).then(function (a) {
            e.location.href = "/checkout"
        })["catch"](function (a) {
            console.log(a)
        })
    }
}]);