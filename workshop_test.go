package workshop

import (
	"testing"

	. "github.com/smartystreets/goconvey/convey"
	"github.com/stretchr/testify/assert"
)

func TestMySum(t *testing.T) {
	total := MySum(5, 5)
	if total != 10 {
		t.Errorf("Sum was incorrect, got: %d, want: %d.", total, 10)
	}
}

func TestMySumConvey(t *testing.T) {
	Convey("When given 2.. integers to add", t, func() {
		So(MySum(5, 5), ShouldEqual, 10)
		So(1<<11, ShouldEqual, 2048)
		So(MySum(5, 1<<100), ShouldEqual, 1<<100+5.)
	})
}

func TestMySumAssert(t *testing.T) {
	assert.Equal(t, MySum(5, 5), 10., "they should be equal")
	assert.Equal(t, MySum(5, 9), 14., "they should be equal")
}
