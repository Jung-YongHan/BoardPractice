<template>
  <div>
    <div v-if="typeof error.detail === 'string'" class="alert alert-danger" role="alert">
      <div>
        {{ error.detail }}
      </div>
    </div>
    <div v-else-if="typeof error.detail === 'object' && error.detail.length > 0" class="alert alert-danger" role="alert">
      <div v-for="(err, i) in error.detail" :key="i">
        <strong>{{ err.loc[1] }}</strong> : {{ err.msg }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    error: {
      type: Object,
      default: () => ({})
    }
  }
};
</script>

<style scoped>
/* Vue에서는 scoped 속성을 사용하여 스타일을 지정합니다. */
.alert {
  padding: 15px;
  margin-bottom: 20px;
  border: 1px solid transparent;
  border-radius: 4px;
}

.alert-danger {
  color: #721c24;
  background-color: #f8d7da;
  border-color: #f5c6cb;
}
</style>
