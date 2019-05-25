<template>
  <div
    class="demo-block"
    :style="hovering ? {boxShadow: '0 0 8px 0 rgba(232, 237, 250, .6), 0 2px 4px 0 rgba(232, 237, 250, .5)'} : {}"
    @mouseenter="hovering = true"
    @mouseleave="hovering = false">
    <div class="header">
      <slot name="header"></slot>
    </div>
    <div class="meta" ref="meta">
      <div class="description" v-if="$slots.default">
        <slot></slot>
      </div>
    </div>
    <div
      class="demo-block-control"
      ref="control"
      :class="{ 'is-fixed': fixedControl }"
      :style="hovering ? {color: '#409EFF', backgroundColor: '#f9fafc'} : {}"
      @click="isExpanded = !isExpanded">
      <transition name="arrow-slide">
        <i :class="[iconClass, { 'hovering': hovering }]"  class="arrow-control" :style="hovering ? {transform: 'translateX(-40px)'} : {}"></i>
      </transition>
      <transition name="text-slide" >
        <span v-show="hovering" class="text-slide-control" :style="hovering ? {transform: 'translateX(-30px)'} : {}">{{controlText}}</span>
      </transition>
    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        hovering: false,
        isExpanded: false,
        fixedControl: false
      };
    },
    methods: {
      scrollHandler() {
        const { top, bottom, left } = this.$refs.meta.getBoundingClientRect();
        this.fixedControl = bottom > document.documentElement.clientHeight &&
          top + 44 <= document.documentElement.clientHeight;
        this.$refs.control.style.left = this.fixedControl ? `${ left }px` : '0';
      },
      removeScrollHandler() {
        this.scrollParent && this.scrollParent.removeEventListener('scroll', this.scrollHandler);
      }
    },
    computed: {
      iconClass() {
        return this.isExpanded ? 'el-icon-caret-top' : 'el-icon-caret-bottom';
      },
      controlText() {
        return this.isExpanded ? 'Hide' : 'Expand';
      },
      codeArea() {
        return this.$el.getElementsByClassName('meta')[0];
      },
      codeAreaHeight() {
        if (this.$el.getElementsByClassName('description').length > 0) {
          return this.$el.getElementsByClassName('description')[0].clientHeight + 20;
        }
        return 0;
      }
    },
    watch: {
      isExpanded(val) {
        this.codeArea.style.height = val ? `${ this.codeAreaHeight + 1 }px` : '0';
        if (!val) {
          this.fixedControl = false;
          this.$refs.control.style.left = '0';
          this.removeScrollHandler();
          return;
        }
        setTimeout(() => {
          this.scrollParent = document.querySelector('.page-component__scroll > .el-scrollbar__wrap');
          this.scrollParent && this.scrollParent.addEventListener('scroll', this.scrollHandler);
          this.scrollHandler();
        }, 200);
      }
    },
  };
</script>

<style>
  .demo-block {
    border: solid 1px #ebebeb;
    border-radius: 3px;
    transition: .2s;
  }

  .header {
      padding: 24px;
    }

  .meta {
      background-color: #fafafa;
      border-top: solid 1px #eaeefb;
      overflow: hidden;
      height: 0;
      transition: height .2s;
    }

  .description {
      padding: 20px;
      font-size: 14px;
      line-height: 22px;
      color: #666;
      word-break: break-word;
      margin: 10px;
    }

  .demo-block-control {
    border-top: solid 1px #eaeefb;
    height: 44px;
    box-sizing: border-box;
    background-color: #fff;
    border-bottom-left-radius: 4px;
    border-bottom-right-radius: 4px;
    text-align: center;
    margin-top: -1px;
    color: #d3dce6;
    cursor: pointer;
    position: relative;
  }

  .arrow-control {
    font-size: 16px;
    line-height: 44px;
    transition: .3s;
  }

  .text-slide-control {
      position: absolute;
      transform: translateX(-30px);
      font-size: 14px;
      line-height: 44px;
      transition: .3s;
      display: inline-block;
    }

  .text-slide-enter, .text-slide-leave-active {
        opacity: 0;
        transform: translateX(10px);
      }

</style>